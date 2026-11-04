from django.shortcuts import render
from .models import Categoria
from django.shortcuts import get_object_or_404



def lista_categorias(request):
    categorias = Categoria.objects.all()

    return render(
        request,
        'categorias/lista.html',
        {'categorias': categorias}
    )
def detalle_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)

    articulos = categoria.articulos.filter(
        estado='publicado'
    )

    return render(
        request,
        'categorias/detalle.html',
        {
            'categoria': categoria,
            'articulos': articulos,
        }
    )