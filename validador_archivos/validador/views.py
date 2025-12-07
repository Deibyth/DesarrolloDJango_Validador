import csv
from io import TextIOWrapper
from django.shortcuts import render
from .forms import ArchivoForm
from .validators import validar_fila


def validar_archivo(request):
    resultado = []

    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)

        if form.is_valid():
            archivo = TextIOWrapper(request.FILES['archivo'].file, encoding='utf-8')
            lector = csv.reader(archivo)

            for numero_fila, fila in enumerate(lector, start=1):
                errores_fila = validar_fila(fila, numero_fila)
                resultado.extend(errores_fila)

            archivo_valido = (len(resultado) == 0)

            mensaje = (
                "Archivo validado correctamente."
                if archivo_valido else
                "Se encontraron los siguientes errores en el archivo:"
            )

            return render(request, "validador/resultado.html", {
                "resultado": resultado,
                "archivo_valido": archivo_valido,
                "mensaje": mensaje
            })

    else:
        form = ArchivoForm()

    return render(request, "validador/upload.html", {"form": form})
