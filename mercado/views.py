from rest_framework import viewsets
from mercado.models import Produto, Category
from mercado.serializer import CategorySerializer, ProdutoSerializer

class ProdutosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os produtos"""
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer