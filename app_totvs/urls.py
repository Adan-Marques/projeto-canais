from django.urls import path
from . import views

urlpatterns = [
    path('home-totver/', views.home_totver, name='home-totver'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
