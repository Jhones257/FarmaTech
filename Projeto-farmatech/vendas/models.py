from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class vendas(models.Model):
    id_venda = models.AutoField(primary_key=True, unique=True)
    data_venda = models.DateField()
    itens_vendidos = models.CharField(max_length=100)
    total_compra = models.FloatField()
    nome_funcionario = models.CharField(max_length=100)
    nome_cliente = models.CharField(max_length=100)
    metodo_pagamento = models.CharField(max_length=100)

    def __str__(self):
        return f'Pedido n. {self.pk}'
    
class ItemVenda(models.Model):
    venda = models.ForeignKey(vendas, on_delete=models.CASCADE)
    produto_nome = models.CharField(max_length=100)
    produto_id = models.PositiveBigIntegerField()
    quantidade = models.PositiveBigIntegerField()
    preco_venda = models.FloatField()

    def __str__(self):
        return f'Item do pedido n. {self.pedido.pk}'