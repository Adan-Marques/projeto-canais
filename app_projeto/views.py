from email import message
from django.shortcuts import render, redirect
from .models import Analista
from .forms import LoginForms, CadastroUserForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request,'usuarios/home.html')

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

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome=form['nome_login'].value()
            senha=form['senha'].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f"{nome} logado(a) com sucesso!")
            return redirect('home')
        else:
            messages.error(request, "Erro ao efetuar login")
            return redirect('login')
        
    return render(request,'login.html', {'form': form})

def cadastro(request):
    form = CadastroUserForms()

    if request.method == 'POST':
        form = CadastroUserForms(request.POST)

        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                messages.error(request, "Senhas não são iguais")
                return redirect('cadastro')

            nome=form["nome_cadastro"].value()
            email=form["email"].value()
            senha=form["senha_1"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, "O usuário já está cadastrado")
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request,"Cadastro efetuado com sucesso")
            return redirect('login')

    return render(request,'usuarios/cadastro.html', {'form': form})

@login_required
def cadastrar_analistas(request):
    return render(request,'usuarios/canais/cadastro-analista.html')

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado")
    return redirect('login')

def home_totver(request):
    return render(request,'usuarios/totvers/home-totver.html')

@login_required
def home_canais(request):
    return render(request,'usuarios/canais/home-canais.html')

@login_required
def dashboard(request):
    return render(request,'usuarios/totvers/dashboard.html')

@login_required
def deletar_analista(request, id):
    analista = Analista.objects.get(id_analista=id)
    analista.delete()
    return redirect('analistas') 

def teste(request):
    return render(request,'usuarios/teste.html')