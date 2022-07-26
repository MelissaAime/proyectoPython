from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from familiares.models import Familia


def mi_familia(request):
    familia = Familia.objects.all()

    template = open(r"C:\Users\Administrator\Desktop\Curso Python\proyectoPython\mi_proyecto\mi_proyecto\templates\familiares.html", "r")
    plantilla = Template(template.read())
    template.close()

    context = Context(familia)

    documento = plantilla.render(context)

    return HttpResponse(documento)


#solo muestra los nombres uno al lado del otro
    # listado = []

    # for f in familia:
    #     listado.append(f.nombre)

    # return HttpResponse(listado)
