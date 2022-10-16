from dataclasses import fields
from rest_framework import serializers
from market.models import Product, Category

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'nome', 'preco', 'marca', 'categoria']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']