from django.shortcuts import render
from .models import Articulo
from django.shortcuts import render, get_object_or_404


def lista_articulos(request):
    articulos = Articulo.objects.filter(
        estado='publicado'
    ).order_by('-fecha_creacion')

    return render(
        request,
        'articulos/lista.html',
        {'articulos': articulos}
    )
def detalle_articulo(request, slug):
    articulo = get_object_or_404(
        Articulo,
        slug=slug,
        estado='publicado'
    )

    return render(
        request,
        'articulos/detalle.html',
        {'articulo': articulo}
    )