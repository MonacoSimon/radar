from django.shortcuts import render, redirect
from .forms import MensajeContactoForm


def formulario_contacto(request):
    if request.method == 'POST':
        formulario = MensajeContactoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('contacto:exito')

    else:
        formulario = MensajeContactoForm()

    return render(
        request,
        'contacto/formulario.html',
        {'formulario': formulario}
    )


def contacto_exito(request):
    return render(request, 'contacto/exito.html')