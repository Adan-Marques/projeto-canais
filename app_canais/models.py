from django.db import models
from app_canais.choices import *
from django.contrib.auth.models import User

class Oferta(models.Model):
    id_oferta = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    segmento = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Modulo(models.Model):
    id_modulo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=False, blank=False)
    oferta = models.ForeignKey(Oferta, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Submodulo(models.Model):
    id_submodulo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=False, blank=False)
    modulo = models.ForeignKey(Modulo, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Unidade(models.Model):
    id_unidade = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Canal(models.Model):
    id_canal = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    cnpj = models.CharField(max_length=20, null=False, blank=False)
    estado = models.CharField(max_length=100, null=False, blank=False)
    regiao = models.CharField(max_length=100, null=False, blank=False)
    tipo = models.CharField(max_length=100, null=False, blank=False)
    contrato = models.CharField(max_length=100, null=False, blank=False)
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Analista(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_analista = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    sobrenome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    celular = models.CharField(max_length=100, null=False, blank=False)
    cargo = models.CharField(max_length=4, choices=CARGO_CHOICES)
    status = models.CharField(max_length=7, null=False, blank=False)
    canal = models.ForeignKey(Canal, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    

class AnalistaSubmodulo(models.Model):
    analista = models.ForeignKey(Analista, on_delete=models.CASCADE)
    submodulo = models.ForeignKey(Submodulo, on_delete=models.CASCADE)

    def __str__(self):
        return self.submodulo
