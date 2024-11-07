from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('listar/', views.listar_produtos, name='listar_produtos'),  # Nova URL para listar produtos
    path('dashboard/', views.dashboard, name='dashboard'),  # Nova URL para o dashboard
]
