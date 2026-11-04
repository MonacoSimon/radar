from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('hola/', views.hola_mundo, name='hola_mundo'),
    path('acerca/', views.acerca, name='acerca'),
]