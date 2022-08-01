from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime

# Templates
def index(request, nombre):

    datos={"fecha_actual": datetime.now(), "usuario": nombre}

    template = open(r"C:\Users\Administrator\Desktop\Curso Python\proyectoPython\mi_proyecto\mi_proyecto\templates\index.html", "r")
    plantilla = Template(template.read())
    template.close()

    # Contexto
    context = Context(datos)

    # Respuesta
    documento = plantilla.render(context)

    # Retornarlo
    return HttpResponse(documento)

def notas(request):

    datos = {"notas": [9, 4, 2, 7, 10], "estudiante": "Meli"}

    plantilla = loader.get_template("notas.html")

    documento = plantilla.render(datos)

    return HttpResponse(documento)

def alumnos (request):
    datos = {"curso": "Python", "alumnos": ["Meli", "Rodri", "Minnie"]}

    plantilla = loader.get_template("alumnos.html")

    documento = plantilla.render(datos)
    
    return HttpResponse(documento)
