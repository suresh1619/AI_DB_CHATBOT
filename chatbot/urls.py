from django.urls import path
from .views import supplier_list, product_list, query_view

urlpatterns = [
    path('', query_view, name="api_home"),
    path('suppliers/', supplier_list, name='supplier-list'),
    path('products/', product_list, name='product-list'),
]
