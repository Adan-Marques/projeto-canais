from email import message
from django.shortcuts import render, redirect
from .forms import LoginForms, CadastroUserForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rolepermissions.roles import assign_role
from rolepermissions.checkers import has_role

@login_required
def home(request):
    return render(request,'usuarios/home.html')

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
            messages.add_message(request, messages.SUCCESS, f"{nome} logado(a) com sucesso!")
            if has_role(usuario, 'totver'):
                return redirect('home-totver')
            elif has_role(usuario, 'canal'):
                return redirect('home-canais')
            else:
                return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, "Erro ao efetuar login")
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

            totvs_dom = "@totvs.com.br"
            if totvs_dom in usuario.email:
                assign_role(usuario, 'totver')
            usuario.save()
            messages.success(request,"Cadastro efetuado com sucesso")
            return redirect('login')

    return render(request,'usuarios/cadastro.html', {'form': form})

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado")
    return redirect('login')

def teste(request):
    return render(request,'usuarios/teste.html')