# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL para a página inicial
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('cadastrar_funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('cadastrar_item_estoque/', views.cadastrar_item_estoque, name='cadastrar_item_estoque'),
    path('editar_item_estoque/<int:id>/', views.editar_item_estoque, name='editar_item_estoque'),
]

