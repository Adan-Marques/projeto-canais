from django.contrib import admin
from django.urls import path
from app_projeto import views
from app_projeto.views import *

urlpatterns = [
    path("admin/", admin.site.urls),

    path('', views.home, name='home'),
    path('login/', views.login, name='login'),	
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    
    path('home-totver/', views.home_totver, name='home-totver'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('home-canais/', views.home_canais, name='home-canais'),
    path('cadastro-analista/', views.cadastro_analista, name='cadastro-analista'),
    path('analistas/',views.analistas, name='analistas')
]
