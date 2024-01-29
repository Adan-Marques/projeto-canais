from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Analista

@login_required
def home_canais(request):
    return render(request,'usuarios/canais/home-canais.html')

@login_required
def cadastrar_analistas(request):
    return render(request,'usuarios/canais/cadastro-analista.html')

@login_required
def analistas(request):
    if request.method == 'POST':
        # Salvar os dados da tela para o banco de dados.
        novo_analista = Analista()  
        novo_analista.nome = request.POST.get('nome')
        novo_analista.email = request.POST.get('email')
        novo_analista.celular = request.POST.get('celular')
        novo_analista.canal = request.POST.get('canal')
        novo_analista.cargo = request.POST.get('cargo')
        novo_analista.oferta = request.POST.get('oferta')
        novo_analista.modulo = request.POST.get('modulo')
        novo_analista.submodulo = request.POST.get('submodulo')
        novo_analista.save()
        # Exibir todoso os analistas já cadastrados em uma nova página
    analistas = {
        'analistas': Analista.objects.all()
    }
    # Retornar os dados para a página de listagem de analistas
    return render(request, 'usuarios/canais/analistas.html', analistas)

@login_required
def deletar_analista(request, id):
    analista = Analista.objects.get(id_analista=id)
    analista.delete()
    return redirect('analistas') 
