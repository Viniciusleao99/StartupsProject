# Generated by Django 5.1.1 on 2024-11-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=50)),
                ('data_aquisicao', models.DateField()),
                ('ciclos_uso', models.IntegerField()),
                ('condicao', models.CharField(choices=[('novo', 'Novo'), ('pouco_usado', 'Pouco Usado'), ('usado', 'Usado'), ('desgastado', 'Desgastado')], max_length=20)),
            ],
        ),
    ]