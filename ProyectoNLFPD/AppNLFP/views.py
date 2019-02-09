from django.shortcuts import render

# Create your views here.
from .models import Jugador
from .models import Equipo
from .models import Estadio

def index(request):
    return render(request,"home/index.html",{})

def about(request):
    context = {

    }
    return render(request,"home/about.html",context)

def listaJugadores(request):
    queryset = Jugador.objects.all()
    context = {
        "lista_jugadores" : queryset
    }
    return render(request,"home/lista-jugadores.html",context)

def detalleJugador(request,id):
    queryset = Jugador.objects.get(id=id)
    context = {
        "object" : queryset
    }
    return render(request,"home/detalle-jugador.html",context)

def buscarJugadorPorPosicion(request,posicion):
    queryset = Jugador.objects.filter(posicion=posicion)
    context = {
        "jugadoresPosicion" : queryset
    }
    return render(request, "home/jugadores-posicion.html",context)

def buscarJugadorPorEquipo(request,equipo):
    queryset = Jugador.objects.filter(equipo=equipo)
    context = {
        "jugadoresEquipo" : queryset
    }
    return render(request, "home/jugadores-equipo.html",context)

def listaEquipos(request):
    queryset = Equipo.objects.all()
    context = {
        "lista_equipos" : queryset
    }
    return render(request,"home/lista-equipos.html",context)

def detalleEquipo(request,id):
    queryset = Equipo.objects.get(id=id)
    context = {
        "object" : queryset
    }
    return render(request,"home/detalle-equipo.html",context)

def listaEstadios(request):
    queryset = Estadio.objects.all()
    context = {
        "lista_estadios" : queryset
    }
    return render(request,"home/lista-estadios.html",context)

def detalleEstadio(request,id):
    queryset = Estadio.objects.get(id=id)
    context = {
        "object" : queryset
    }
    return render(request,"home/detalle-estadio.html",context)