from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def home_canais(request):
    return render(request,'home-canais.html')

@login_required
def cadastrar_analistas(request):
    return render(request,'cadastrar-analista.html')

@login_required
def analistas(request):
    if request.method == 'POST':

        novo_analista = Analista()  
        novo_analista.nome = request.POST.get('nome')
        novo_analista.sobrenome = request.POST.get('sobrenome')
        novo_analista.email = request.POST.get('email')
        novo_analista.celular = request.POST.get('celular')
        novo_analista.cargo = request.POST.get('cargo')
        novo_analista.status = request.POST.get('status')
        novo_analista.save()

    dados_analistas = Analista.objects.filter(user=request.user)
    #submodulo_analistas = AnalistaSubmodulo.objects.filter(analista=novo_analista.id_analista)

    return render(request, 'analistas.html',
                  {'dados_analistas': dados_analistas,})

@login_required
def deletar_analista(request, id):
    analista = Analista.objects.get(id_analista=id)
    analista.delete()
    return redirect('analistas') 
