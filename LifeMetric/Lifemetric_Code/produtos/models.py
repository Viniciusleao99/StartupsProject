from django.utils import timezone
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    data_aquisicao = models.DateField()
    ciclos_uso = models.IntegerField()
    condicao = models.CharField(max_length=20, choices=[
        ('novo', 'Novo'),
        ('pouco_usado', 'Pouco Usado'),
        ('usado', 'Usado'),
        ('desgastado', 'Desgastado'),
    ])

    def calcular_qualidade_vida(self):
        # Exemplo de cálculo simples de qualidade de vida
        dias_desde_aquisicao = (timezone.now().date() - self.data_aquisicao).days
        fator_condicao = {"Novo": 1.0, "Bom": 0.8, "Usado": 0.5, "Desgastado": 0.2}
        condicao_fator = fator_condicao.get(self.condicao, 0.5)

        # Fórmula: quanto maior o tempo e os ciclos, menor a qualidade de vida
        qualidade_vida = max(0, (100 - dias_desde_aquisicao * 0.1 - self.ciclos_uso * 0.5) * condicao_fator)
        return round(qualidade_vida, 2)

    def __str__(self):
        return self.nome
