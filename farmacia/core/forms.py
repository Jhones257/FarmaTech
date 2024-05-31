# core/forms.py
from django import forms
from .models import Funcionario, Estoque

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'cpf_funcionario', 'numero_telefone', 'endereco', 'data_nasc', 'email', 'data_admissao', 'salario']

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['id_produtoEstoque', 'qtq_estoque', 'qtq_limite']
