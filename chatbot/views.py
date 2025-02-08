from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Supplier, Product
from .serializers import SupplierSerializer, ProductSerializer
from .utils import workflow, QueryState


@api_view(['GET', 'POST'])
def supplier_list(request):
    if request.method == 'GET':
        suppliers = Supplier.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def query_view(request):
    """
    API view to process user queries using the chatbot.
    """
    user_query = request.data.get("query", "")
    
    if not user_query:
        return Response({"error": "Query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
    
    
    initial_state = QueryState(query=user_query).to_dict()
    final_state = workflow.invoke(initial_state)
    
    return Response({
        "query": user_query,
        "generated_sql": final_state["sql_query"],
        "results": final_state["results"],
        "summary": final_state["summary"]
    }, status=status.HTTP_200_OK)