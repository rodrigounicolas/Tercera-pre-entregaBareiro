from django.shortcuts import render
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# Create your views here.
def home(request):
    return render(request, "aplicacion/index.html")

def institucion(request):
    contexto = {'Institucion': Institucion.objects.all()}
    return render(request, "aplicacion/institucion.html", contexto)

def tablaGoleadores(request):
    tabla_goleadores = TablaGoleadores.objects.all()
    contexto = {'tablaGoleadores': tabla_goleadores}
    return render(request, "aplicacion/TablaGoleadores.html", contexto)

def posicion(request):
    contexto = {'Posicion': Posicion.objects.all()}
    return render(request, "aplicacion/Posicion.html", contexto)

def acerca(request):
    return render(request, "aplicacion/acerca.html")

def buscarInstitucion(request):
    return render(request, "aplicacion/buscar.html")

def encontrarInstitucion(request):
    buscar_query = request.GET.get("buscar", None)
    if buscar_query:
        instituciones = Institucion.objects.filter(nombre__icontains=buscar_query)
    else:
        instituciones = Institucion.objects.all()
    
    contexto = {"institucion": instituciones}
    return render(request, "aplicacion/Institucion.html", contexto)

def buscarPosicion(request):
    return render(request, "aplicacion/buscarposicion.html")

def encontrarPosicion(request):
    buscar_query = request.GET.get("buscar", None)
    if buscar_query:
        posiciones = Posicion.objects.filter(equipo__icontains=buscar_query)
    else:
        posiciones = Posicion.objects.all()
    
    contexto = {"posiciones": posiciones}
    return render(request, "aplicacion/Posicion.html", contexto)








#______ Institucion

class InstitucionList(ListView):
    model = Institucion
    

class InstitucionCreate(CreateView):
    model = Institucion
    fields = ["nombre", "direccion"]
    success_url = reverse_lazy("Institucion")

class InstitucionUpdate(UpdateView):
    model = Institucion
    fields = ["nombre", "direccion"]
    success_url = reverse_lazy("Institucion")
    
class InstitucionDelete(DeleteView):
    model = Institucion
    success_url = reverse_lazy("Institucion")

class PosicionList(ListView):
    model = Posicion

class PosicionCreate(CreateView):
    model = Posicion
    fields = ["equipo", "puntos"]
    success_url = reverse_lazy("Posicion")
    
class PosicionUpdate(UpdateView):
    model = Posicion
    fields = ["equipo", "puntos"]
    success_url = reverse_lazy("Posicion")

class PosicionDelete(DeleteView):
    model = Posicion
    success_url = reverse_lazy("Posicion")
    
class TablaGoleadoresList(ListView):
    model = TablaGoleadores

class TablaGoleadoresCreate(CreateView):
    model= TablaGoleadores
    fields = ["jugador", "goles"]
    success_url = reverse_lazy("TablaGoleadores")

#__forms

def institucionForm(request):
    if request.method == "POST": 
        miForm = InstitucionForm(request.POST)
        if miForm.is_valid():
            institucion_nombre = miForm.cleaned_data.get("nombre")
            institucion_direccion = miForm.cleaned_data.get("direccion")
            institucion = Institucion(nombre=institucion_nombre, direccion=institucion_direccion)
            institucion.save()
            return render(request, "aplicacion/index.html")
    else:
        miForm = InstitucionForm()
        
    return render(request, "aplicacion/institucionForm.html", {"form": miForm} )

def posicionForm(request):
    if request.method == "POST": 
        miForm = PosicionForm(request.POST)
        if miForm.is_valid():
            posicion_equipo = miForm.cleaned_data.get("equipo")
            posicion_puntos = miForm.cleaned_data.get("puntos")
            posicion = Posicion(nombre=posicion_equipo, direccion=posicion_puntos)
            posicion.save()
            return render(request, "aplicacion/index.html")
    else:
        miForm = PosicionForm()
        
    return render(request, "aplicacion/posicionForm.html", {"form": miForm} )
