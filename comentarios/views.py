from django.shortcuts import render, redirect, get_object_or_404
from articulos.models import Articulo
from .forms import ComentarioForm


def crear_comentario(request, articulo_id):

    articulo = get_object_or_404(
        Articulo,
        id=articulo_id,
        estado='publicado'
    )

    if request.method == 'POST':
        formulario = ComentarioForm(request.POST)

        if formulario.is_valid():
            comentario = formulario.save(commit=False)
            comentario.articulo = articulo
            comentario.estado = 'pendiente'
            comentario.save()

            return redirect(
                'articulos:detalle',
                slug=articulo.slug
            )

    else:
        formulario = ComentarioForm()

    return render(
        request,
        'comentarios/formulario.html',
        {
            'formulario': formulario,
            'articulo': articulo,
        }
    )