from django.urls import path
from aplicacion.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("cursos/", cursos, name="cursos"),
    path("estudiantes/", estudiante),
    path("entregables/", entregable),
    path("formulario/", formulario, name="formulario"),
    path("crear/curso/", crear_curso, name="curso_crear"),
    path("buscar/", formulario_busqueda, name=" formBusqueda"),
    path("resultados/", buscar, name="buscar_curso"),
    path("curso/borrar/<id_curso>/", borrar_curso, name="borrar_curso"),
    # path("infoformulario/", info_formulario, name="infoformulario")

    path("profesores/", ProfesoresList.as_view(), name="profesores"),
    path("profesores/crear/", ProfesorCreate.as_view(), name="profesor_create"),
    path("profesores/actualizar/<pk>", ProfesorUpdate.as_view(), name="profesor_update"),
    path("profesores/borrar/<pk>", ProfesorDelete.as_view(), name="profesor_delete"),
    path("profesores/<pk>", ProfesorDetail.as_view(), name="profesor_detail"),
]