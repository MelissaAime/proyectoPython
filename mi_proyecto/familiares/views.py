from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from familiares.models import Familia


def mi_familia(request):
    familia = Familia.objects.all()

# Sin conexion con el template
    # listado_nombres= []

    # for f in familia:
    #     listado_nombres.append(f"Familiar: {f.id}, Nombre: {f.nombre}, Edad: {f.edad}, Parentezco: {f.parentezco}, ")

    # return HttpResponse(listado_nombres)


# Conectando con el template, no funciona:
        
    plantilla = loader.get_template("familiares.html")

    documento = plantilla.render({"familia": familia})

    return HttpResponse(documento)
