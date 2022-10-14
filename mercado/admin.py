from django.contrib import admin
from mercado.models import Produto

class Produtos(admin.ModelAdmin):
    list_display = ('id', 'categoria', 'nome', 'preco', 'marca')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'marca')

admin.site.register(Produto, Produtos)