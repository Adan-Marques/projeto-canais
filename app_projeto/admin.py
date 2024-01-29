from django.contrib import admin
from .models import *
from app_canais.models import Analista

admin.site.register(Analista)
admin.site.register(Unidade)
admin.site.register(Canal)
admin.site.register(Oferta)
