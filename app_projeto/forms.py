from turtle import textinput
from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "input-form",
                "placeholder": "Digite seu usuário",
            }
        )
    )   
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "input-form",
                "placeholder": "Digite sua senha"
            }
        )
    )

class CadastroUserForms(forms.Form):
    nome_cadastro=forms.CharField(
        label="Nome de Cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "input-form",
                "placeholder": "Ex.: Pedro Silva"
            }
        )
    )   
    email=forms.EmailField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
            "class": "input-form",
            "placeholder": "Ex.: pedrosilva@email.com"
            }
        ) 
    )
    senha_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "input-form",
                "placeholder": "Digite sua senha"
            }
        )
    )
    senha_2 = forms.CharField(
        label="Confirmação de senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "input-form",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )
