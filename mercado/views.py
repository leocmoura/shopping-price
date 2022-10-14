from rest_framework import viewsets
from mercado.models import Produtos
from mercado.serializer import ProdutoSerializer
class ProdutosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os produtos"""
    queryset = Produtos.objects.all()
    serializer_class = ProdutoSerializer