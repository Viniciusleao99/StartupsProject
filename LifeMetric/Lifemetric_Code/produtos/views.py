from django.shortcuts import render, redirect
from .models import Produto
from django.contrib import messages

def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        categoria = request.POST.get('categoria')
        marca = request.POST.get('marca')
        data_aquisicao = request.POST.get('data_aquisicao')
        ciclos_uso = request.POST.get('ciclos_uso')
        condicao = request.POST.get('condicao')

        # Cria um novo produto com os dados do formulário
        Produto.objects.create(
            nome=nome,
            descricao=descricao,
            preco=preco,
            categoria=categoria,
            marca=marca,
            data_aquisicao=data_aquisicao,
            ciclos_uso=ciclos_uso,
            condicao=condicao
        )
        
        # Exibe uma mensagem de sucesso e redireciona para o formulário
        messages.success(request, "Produto cadastrado com sucesso!")
        return redirect('cadastrar_produto')
    
    return render(request, 'produtos/cadastrar_produto.html')

def listar_produtos(request):
    # Busca todos os produtos do banco de dados
    produtos = Produto.objects.all()
    # Passa os produtos para o template de listagem
    return render(request, 'produtos/listar_produtos.html', {'produtos': produtos})

def dashboard(request):
    produtos = Produto.objects.all()
    produtos_qualidade_vida = [
        {
            'nome': produto.nome,
            'qualidade_vida': produto.calcular_qualidade_vida(),
            'condicao': produto.condicao,
            'data_aquisicao': produto.data_aquisicao,
            'ciclos_uso': produto.ciclos_uso,
        }
        for produto in produtos
    ]
    return render(request, 'produtos/dashboard.html', {'produtos_qualidade_vida': produtos_qualidade_vida})
