from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from familiares.models import Familia


def mi_familia(request):
    familia = Familia.objects.all()
        
    plantilla = loader.get_template("familiares.html")

    documento = plantilla.render({"familia": familia})

    return HttpResponse(documento)
