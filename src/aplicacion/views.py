from django.shortcuts import render
from django.http import HttpResponse
from aplicacion.models import Curso, Estudiante, Profesor, Entregable

# Create your views here.
def cursos(request):
    cursos = Curso.objects.all()

    lista_cursos_nombre = []

    for curso in cursos:
        lista_cursos_nombre.append(curso.nombre)
    return HttpResponse(lista_cursos_nombre)


def inicio(request):
    return render(request, "aplicacion/index.html", {"mensaje": "Hola como estas"})

def estudiante(request):
    return HttpResponse ("Vista estudiante")

def profesor(request):
    return HttpResponse ("Vista profesor")

def entregable(request):
    return HttpResponse ("Vista entregable")