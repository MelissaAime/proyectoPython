from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime

def hello(request):
    return HttpResponse("Hello")

def hora_actual(request):
    hora = datetime.now()
    return HttpResponse(f"<h1>{hora}</h1>")

def hello_name(request, name):
    return HttpResponse(f"Hola {name}")

def calcular_nacimiento(request, edad):

    anio_actual = 2022
    anio_nacimiento = anio_actual - int(edad)

    return HttpResponse(f"Ud. ha nacido en el anio {anio_nacimiento}")

# Templates
def inicio(request):
    template = open(r"C:\Users\Administrator\Desktop\Curso Python\proyectoPython\mi_proyecto\mi_proyecto\templates\index.html", "r")
    plantilla = Template(template.read())
    template.close()

    # Contexto
    context = Context()

    # Respuesta
    documento = plantilla.render(context)

    # Retornarlo
    return HttpResponse(documento)
