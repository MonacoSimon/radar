from django.shortcuts import render
from .models import Articulo
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator


def lista_articulos(request):
    articulos = Articulo.objects.filter(
        estado='publicado'
    ).order_by('-fecha_creacion')

    paginador = Paginator(articulos, 6)

    numero_pagina = request.GET.get('page')

    articulos_paginados = paginador.get_page(numero_pagina)

    return render(
        request,
        'articulos/lista.html',
        {'articulos': articulos_paginados}
    )

def detalle_articulo(request, slug):
    articulo = get_object_or_404(
        Articulo,
        slug=slug,
        estado='publicado'
    )

    comentarios = articulo.comentarios.filter(
        estado='aprobado'
    )

    return render(
        request,
        'articulos/detalle.html',
        {
            'articulo': articulo,
            'comentarios': comentarios,
        }
    )