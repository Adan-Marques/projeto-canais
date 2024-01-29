from django.urls import path
from . import views


urlpatterns = [
    path('home-canais/', views.home_canais, name='home-canais'),
    path('cadastro-analista/', views.cadastrar_analistas, name='cadastro-analista'),
    path('analistas/',views.analistas, name='analistas'),
    path('deletar-analista/<int:id>/', views.deletar_analista, name='deletar-analista'),
]