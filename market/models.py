from email.policy import default
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Product(models.Model):
    # CATEGORIA = (
    #     ('0', 'Escolha uma categoria'),
    #     ('1', 'Padaria'),
    #     ('2', 'Alimentos (cereais e grãos)'),
    #     ('3', 'Congelados e frios'),
    #     ('4', 'Hortifruti'),
    #     ('5', 'Produtos de limpeza'),
    #     ('6', 'Higiene pessoal'),
    #     ('7','Bebidas'),
    #     ('8','Papelaria'),
    # )
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)
    nome = models.CharField(max_length=20)
    preco = models.FloatField()
    marca = models.CharField(max_length=15)
    # creation_date = models.DateField()

    def __str__(self):
        return self.nome
