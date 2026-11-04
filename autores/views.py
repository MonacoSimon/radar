from django.shortcuts import render
from .models import Autor


def lista_autores(request):
    autores = Autor.objects.filter(activo=True)

    return render(
        request,
        'autores/lista.html',
        {'autores': autores}
    )
from django.shortcuts import get_object_or_404


def detalle_autor(request, autor_id):
    autor = get_object_or_404(
        Autor,
        id=autor_id,
        activo=True
    )

    articulos = autor.articulos.filter(
        estado='publicado'
    )

    return render(
        request,
        'autores/detalle.html',
        {
            'autor': autor,
            'articulos': articulos,
        }
    )