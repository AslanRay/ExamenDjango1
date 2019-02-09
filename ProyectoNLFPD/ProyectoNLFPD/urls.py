"""ProyectoNLFPD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppNLFP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index_view"),
    path('about/',views.about,name="about_view"),
    path('lista-jugadores/',views.listaJugadores,name="lista_jugadores_view"),
    path('detalle-jugador/<int:id>',views.detalleJugador,name="detalle_jugador_view"),
    path('jugadores-posicion/<str:posicion>',views.buscarJugadorPorPosicion,name="jugadores_posicion_view"),
    path('jugadores-equipo/<str:equipo>',views.buscarJugadorPorEquipo,name="jugadores_equipo_view"),
    path('lista-equipos/',views.listaEquipos,name="lista_equipos_view"),
    path('detalle-equipo/<int:id>',views.detalleEquipo,name="detalle_equipo_view"),
    path('lista-estadios/',views.listaEstadios,name="lista_estadios_view"),
    path('detalle-estadio/<int:id>',views.detalleEstadio,name="detalle_estadio_view"),
]
