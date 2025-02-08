import google.generativeai as genai
import re
from langgraph.graph import StateGraph
from django.db import connection

genai.configure(api_key="AIzaSyAUsOjPWJVRyusiucDsa-74PAYv1k5W0Fk")
model = genai.GenerativeModel("gemini-1.5-flash")

class QueryState:
    def __init__(self, query=""):
        self.query = query
        self.sql_query = ""
        self.results = []
        self.summary = ""

    def to_dict(self):
        return {
            "query": self.query,
            "sql_query": self.sql_query,
            "results": self.results,
            "summary": self.summary,
        }

    @staticmethod
    def from_dict(state_dict):
        state = QueryState(state_dict.get("query", ""))
        state.sql_query = state_dict.get("sql_query", "")
        state.results = state_dict.get("results", [])
        state.summary = state_dict.get("summary", "")
        return state

def generate_sql(state: dict) -> dict:
    state_obj = QueryState.from_dict(state)
    schema_info = """
    The following are the table names and their structures:

    Table Name: chatbot_supplier
    Fields:
        - id: INT (Primary Key)
        - name: VARCHAR(255)
        - contact_info: TEXT
        - product_categories_offered: TEXT
    Relationships:
        - products: ForeignKey to Product (one-to-many)

    Table Name: chatbot_product
    Fields:
        - id: INT (Primary Key)
        - name: VARCHAR(255)
        - brand: VARCHAR(255)
        - price: DECIMAL(10,2)
        - category: VARCHAR(255)
        - description: TEXT
        - supplier_id: INT (Foreign Key to Supplier)
    """
    prompt = f"""
    The database schema is as follows: {schema_info}.
    Write an SQL query to {state_obj.query}.
    Provide only the SQL query, no explanation.
    Use case-insensitive filtering when applicable (e.g. LOWER() for MySQL).
    """
    response = model.generate_content(prompt)
    sql_query = response.text.strip() if response and response.text else ""
    sql_query = re.sub(r'^```sql\s*', '', sql_query)
    sql_query = re.sub(r'\s*```$', '', sql_query)
    state_obj.sql_query = sql_query
    return state_obj.to_dict()

def execute_sql(state: dict) -> dict:
    state_obj = QueryState.from_dict(state)
    with connection.cursor() as cursor:
        cursor.execute(state_obj.sql_query)
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    state_obj.results = results
    return state_obj.to_dict()

def summarize_results(state: dict) -> dict:
    state_obj = QueryState.from_dict(state)
    formatted_data = "\n".join(
        [", ".join([f"{col}: {value}" for col, value in row.items()]) for row in state_obj.results]
    )
    prompt = f"""
    Summarize the following database results for the user query: "{state_obj.query}".
    Data:
    {formatted_data}
    Your summary should:
    - Highlight key details such as product brands, categories, and price ranges.
    - Be concise, clear, and meaningful.
    - Avoid unnecessary information. if formatted data is none give no such data is found
    """
    response = model.generate_content(prompt)
    state_obj.summary = response.text.strip() if response and response.text else "No summary available."
    return state_obj.to_dict()

graph = StateGraph(dict)  
graph.add_node("generate_sql", generate_sql)
graph.add_node("execute_sql", execute_sql)
graph.add_node("summarize_results", summarize_results)

graph.add_edge("generate_sql", "execute_sql")
graph.add_edge("execute_sql", "summarize_results")

graph.set_entry_point("generate_sql")
workflow = graph.compile()

initial_state = QueryState(query="Show me all products under brand Apple").to_dict()
final_state = workflow.invoke(initial_state)
