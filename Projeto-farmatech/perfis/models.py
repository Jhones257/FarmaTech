from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class perfil_usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    email = models.EmailField()
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()
    data_nascimento = models.DateField()
    salario = models.DecimalField(max_digits=7, decimal_places=2)
    cargo = models.CharField(
        max_length=50,
        choices=[
            ('gerente', 'Gerente'),
            ('farmaceutico', 'Farmacêutico'),
            ('balconista', 'Balconista'),
        ]
    )
    data_admissao = models.DateField()

    def __str__(self):
        return f'{self.nome.first_name} {self.nome.last_name}'
    def clean(self):
        pass

class perfil_cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, blank=True)
    telefone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f'{self.nome.first_name} {self.nome.last_name}'
    def clean(self):
        pass