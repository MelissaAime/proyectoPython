from django.shortcuts import render
from django.http import HttpResponse
from aplicacion.models import Curso

# Create your views here.
def lista_cursos(request):
    cursos = Curso.objects.all()

    lista_cursos_nombre = []

    for curso in cursos:
        lista_cursos_nombre.append(curso.nombre)
    return HttpResponse(lista_cursos_nombre)
