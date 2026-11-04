from django.shortcuts import render
from articulos.models import Articulo
from categorias.models import Categoria


def hola_mundo(request):
    return render(request, 'paginas/hola.html')


def inicio(request):
    articulos = Articulo.objects.filter(
        estado='publicado'
    ).order_by('-fecha_creacion')[:5]

    categorias = Categoria.objects.all()

    contexto = {
        'articulos': articulos,
        'categorias': categorias,
    }

    return render(request, 'paginas/inicio.html', contexto)

def acerca(request):
    return render(request, 'paginas/acerca.html')