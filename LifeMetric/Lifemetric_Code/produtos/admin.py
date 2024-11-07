from django.contrib import admin
from .models import Produto

# Registra o modelo Produto para que ele apareça no painel de administração
admin.site.register(Produto)