from rest_framework import serializers
from mercado.models import Produtos

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = ['__all__']