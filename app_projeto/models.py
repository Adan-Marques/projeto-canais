from django.db import models
from .choices import *
from django import forms

class Analista(models.Model):
    id_analista = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    celular = models.CharField(max_length=255, null=False, blank=False)
    canal = models.CharField(max_length=255, null=False, blank=False)
    cargo = models.CharField(max_length=255)
    oferta = models.CharField(max_length=255, choices=OFERTA_CHOICES, null=False, blank=False)
    modulo = models.CharField(max_length=255)
    submodulo = models.CharField(max_length=255)

class Unidade(models.Model):
    id_unidade = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=False, blank=False)

class Canal(models.Model):
    id_canal = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=False, blank=False)
    unidade = models.ForeignKey(Unidade, on_delete=models.DO_NOTHING)

class Oferta(models.Model):
    id_oferta = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=False, blank=False)
