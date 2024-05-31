from django.shortcuts import render

# Create your views here.
# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Funcionario, Estoque, Produto
from .forms import FuncionarioForm, EstoqueForm


def user_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'core/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def cadastrar_funcionario(request):
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FuncionarioForm()
    return render(request, 'core/cadastrar_funcionario.html', {'form': form})


def cadastrar_item_estoque(request):
    if request.method == "POST":
        form = EstoqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EstoqueForm()
    return render(request, 'core/cadastrar_item_estoque.html', {'form': form})


def editar_item_estoque(request, id):
    estoque = Estoque.objects.get(id_estoque=id)
    if request.method == "POST":
        form = EstoqueForm(request.POST, instance=estoque)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EstoqueForm(instance=estoque)
    return render(request, 'core/editar_item_estoque.html', {'form': form})

# core/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

