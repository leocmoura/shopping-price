# Generated by Django 4.1.2 on 2022-10-14 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mercado', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Produtos',
            new_name='Produto',
        ),
    ]