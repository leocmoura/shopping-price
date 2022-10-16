from rest_framework import viewsets
from market.models import Product, Category
from market.serializer import CategorySerializer, ProductsSerializer

class ProductsViewSet(viewsets.ModelViewSet):
    """Exibindo todos os produtos"""
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer