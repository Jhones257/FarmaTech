# Generated by Django 5.0.6 on 2024-05-26 21:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nome_cliente', models.CharField(max_length=250)),
                ('cpf_cliente', models.CharField(max_length=250)),
                ('telefone_cliente', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id_funcionario', models.AutoField(primary_key=True, serialize=False)),
                ('nome_funcionario', models.CharField(max_length=250)),
                ('cpf_funcionario', models.CharField(max_length=250)),
                ('telefone_funcionario', models.CharField(max_length=250)),
                ('endereco_funcionario', models.CharField(max_length=250)),
                ('dataNasc_funcionario', models.DateField()),
                ('email_funcionario', models.CharField(max_length=250)),
                ('cargo_funcionario', models.CharField(max_length=250)),
                ('dataAdmissao', models.DateField()),
                ('salario_funcionario', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id_produto', models.AutoField(primary_key=True, serialize=False)),
                ('nome_produto', models.CharField(max_length=250)),
                ('descricao_produto', models.CharField(max_length=500)),
                ('preco_produto', models.FloatField()),
                ('categoria_produto', models.CharField(max_length=250)),
                ('dataValidade', models.DateField()),
                ('nomeForncedor', models.CharField(max_length=250)),
                ('emailFornecedor', models.CharField(max_length=250)),
                ('prescricao_produto', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id_estoque', models.AutoField(primary_key=True, serialize=False)),
                ('quantidade_estoque', models.IntegerField()),
                ('qtdMinima', models.IntegerField()),
                ('idProduto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_farmacia.produto')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id_venda', models.AutoField(primary_key=True, serialize=False)),
                ('nomeCliente', models.CharField(max_length=250)),
                ('itens_venda', models.CharField(max_length=1000)),
                ('total_venda', models.FloatField()),
                ('metodoPagamento', models.CharField(max_length=250)),
                ('idFuncionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_farmacia.funcionario')),
            ],
        ),
    ]
