from django.db import models
import uuid

# Create your models here.
# core/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    id_funcionario = models.AutoField(primary_key=True)
    cpf_funcionario = models.CharField(max_length=14, unique=True)
    numero_telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)
    data_nasc = models.DateField()
    email = models.EmailField(unique=True)
    data_admissao = models.DateField()
    salario = models.FloatField()

class Gerente(models.Model):
    id_gerente = models.AutoField(primary_key=True)
    email_gerente = models.EmailField(unique=True)
    senha_gerente = models.CharField(max_length=128)

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome_cliente = models.CharField(max_length=255)
    cpf_cliente = models.CharField(max_length=14, unique=True)
    telefone_cliente = models.CharField(max_length=15)

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    id_produto = models.AutoField(primary_key=True)
    descricao = models.TextField()
    preco_produto = models.FloatField()
    data_validade = models.DateField()
    categoria = models.CharField(max_length=255)
    prescricao = models.BooleanField(default=False)
    nome_fornecedor = models.CharField(max_length=255)
    email_fornecedor = models.EmailField()

class Estoque(models.Model):
    id_estoque = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_produtoEstoque = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtq_estoque = models.IntegerField()
    qtq_limite = models.IntegerField()

class Vendas(models.Model):
    id_venda = models.AutoField(primary_key=True)
    data_venda = models.DateField()
    itens_vendidos = models.TextField()
    total_compra = models.FloatField()
    nome_funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    nome_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    metodo_pagamento = models.CharField(max_length=50)
