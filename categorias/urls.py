from django.urls import path
from . import views

app_name = 'categorias'

urlpatterns = [
    path('', views.lista_categorias, name='lista'),
    path('<slug:slug>/', views.detalle_categoria, name='detalle'),
]