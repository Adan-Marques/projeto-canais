from django.db import models
from app_projeto.models import Oferta

class Analista(models.Model):
    id_analista = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=False, blank=False)
    sobrenome = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    celular = models.CharField(max_length=255, null=False, blank=False)
    canal = models.CharField(max_length=255, null=False, blank=False)
    cargo = models.CharField(max_length=255)
    oferta = models.ForeignKey(Oferta, on_delete=models.DO_NOTHING)
    modulo = models.CharField(max_length=255)
    submodulo = models.CharField(max_length=255)