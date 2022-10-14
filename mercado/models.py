from email.policy import default
from django.db import models

class Produto(models.Model):
    CATEGORIA = (
        ('0', 'Escolha uma categoria'),
        ('1', 'Padaria'),
        ('2', 'Alimentos (cereais e grãos)'),
        ('3', 'Congelados e frios'),
        ('4', 'Hortifruti'),
        ('5', 'Produtos de limpeza'),
        ('6', 'Higiene pessoal'),
        ('7','Bebidas'),
        ('8','Papelaria'),
    )
    categoria = models.CharField(max_length=1, choices=CATEGORIA, blank=False, null=False, default='0')
    nome = models.CharField(max_length=20)
    preco = models.FloatField()
    marca = models.CharField(max_length=15)

    def __str__(self):
        return self.nome