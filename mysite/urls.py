from django.contrib import admin
from django.urls import path, include
from app_projeto import views
from app_projeto.views import *

urlpatterns = [
    path("admin/", admin.site.urls),

    path('', views.home, name='home'),
    path('login/', views.login, name='login'),	
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    

    path('totvs/', include('app_totvs.urls')),

    path('canais/', include('app_canais.urls')),

    path('teste/', views.teste, name='teste'),

]
