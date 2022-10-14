from rest_framework import viewsets
from mercado.models import Produto
from mercado.serializer import ProdutoSerializer

class ProdutosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os produtos"""
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer