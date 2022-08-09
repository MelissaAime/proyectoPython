from django.forms import Form, IntegerField, CharField, EmailField

class CursoFormulario(Form):
    nombre = CharField()
    camada = IntegerField()

    
class ProfesorFormulario(Form):
    nombre = CharField(max_length=30)
    apellido = CharField(max_length=30)
    email = EmailField()
    profesion = CharField(max_length=30)