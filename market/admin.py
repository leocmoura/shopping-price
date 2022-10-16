from django.contrib import admin
from market.models import Product, Category

class Products(admin.ModelAdmin):
    list_display = ('id', 'categoria', 'nome', 'preco', 'marca')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'marca')

admin.site.register(Product, Products)

class Categorys(admin.ModelAdmin):
    list_display = ('id', 'category_name')

admin.site.register(Category, Categorys)