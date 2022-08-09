from django.shortcuts import render, redirect
from django.http import HttpResponse
from aplicacion.models import Curso, Estudiante, Profesor, Entregable
from aplicacion.forms import CursoFormulario
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
def estudiante(request):
    return HttpResponse ("Vista estudiante")



def entregable(request):
    return HttpResponse ("Vista entregable")

def inicio(request):
    return render(request, "aplicacion/index.html")

def cursos(request):
    cursos = Curso.objects.all()

    lista_cursos_nombre = []

    for curso in cursos:
        lista_cursos_nombre.append(curso.nombre)
    return HttpResponse(lista_cursos_nombre)

def formulario(request):
    return render(request, "aplicacion/formulario.html")

def crear_curso(request):

    if request.method == 'GET':
        formulario = CursoFormulario()
        return render(request, "aplicacion/formulario.html", {"formulario": formulario})
    
    else:
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data
            nombre = data.get('nombre')
            camada = data.get('camada')
            curso = Curso(nombre= nombre, camada= camada)
            curso.save()

            return render(request, "aplicacion/index.html")
        
        else:
            return HttpResponse("formulario no valido")

def formulario_busqueda(request):
    return render (request, "aplicacion/form_busqueda.html")

def buscar(request):
    curso_nombre = request.GET.get("curso", None)
    camada = request.GET.get("camada", None)

    if not curso_nombre:
        return HttpResponse("No indicaste ningún nombre")
    
    cursos_lista = Curso.objects.filter(nombre__icontains=curso_nombre)

    if camada:
        cursos_lista = cursos_lista.filter(camada=camada)
        
    return render(request, "aplicacion/resultado_busq.html", {"cursos": cursos_lista})


def borrar_curso(request, id_curso):
    try:
        curso = Curso.objects.get(id=id_curso)
        curso.delete()
        return redirect("cursos")
    except:
        return redirect("inicio")

def editar_curso(request, id_curso):
    if request.method == "GET":
        formulario = CursoFormulario()
        context = {"formulario" : formulario}
        return render(request, "aplicacion/cursos.html", context)
    else:
        formulario = CursoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            try:
                curso = Curso.objects.get(id=id_curso)
                curso.nombre= data.get("nombre")
                curso.camada= data.get("camada")
                curso.save()
            except: 
                return


      
# def profesor(request):
#     return HttpResponse ("Vista profesor")

class ProfesoresList(ListView):
    model = Profesor
    template_name = "aplicacion/profesores_list.html"

class ProfesorDetail(DetailView):
    model = Profesor
    template_name = "aplicacion/profesor_detail.html"

class ProfesorCreate(CreateView):
    model = Profesor
    success_url = "/aplicacion/profesores/"
    fields = ['nombre', 'apellido', 'email', 'profesion']

class ProfesorUpdate(UpdateView):
    model = Profesor
    success_url = "/aplicacion/profesores/"
    fields = ['nombre', 'apellido', 'email', 'profesion']

class ProfesorDelete(DeleteView):
    model = Profesor
    success_url = "/aplicacion/profesores/"

