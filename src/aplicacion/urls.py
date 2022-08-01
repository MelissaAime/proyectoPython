from django.urls import path
from aplicacion.views import *

urlpatterns = [
    path("", inicio),
    path("cursos/", cursos),
    path("estudiantes/", estudiante),
    path("profesor/", profesor),
    path("entregables/", entregable)
]