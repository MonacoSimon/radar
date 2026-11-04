from django.urls import path
from . import views

app_name = 'autores'

urlpatterns = [
    path('', views.lista_autores, name='lista'),
]