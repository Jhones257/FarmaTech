from django.db import models

# Create your models here.

class produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade = models.IntegerField()
    id_produto = models.AutoField(primary_key=True, unique=True)
    data_validade = models.DateField()
    categoria = models.CharField(
        max_length=50,
        choices=[
            ('Medicamento', 'Medicamento'),
            ('Higiene', 'Higiene'),
            ('Alimento', 'Alimento'),
            ('Cosmético', 'Cosmético'),
            ('Outro', 'Outro'),
        ]
    )
    prescrição = models.BooleanField()
    nome_fornecedor = models.CharField(max_length=50)
    email_fornecedor = models.EmailField()
    def __str__(self):
        return self.nome