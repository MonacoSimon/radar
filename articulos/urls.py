from django.urls import path
from . import views

app_name = 'articulos'

urlpatterns = [
    path('', views.lista_articulos, name='lista'),
    path('<slug:slug>/', views.detalle_articulo, name='detalle'),
]