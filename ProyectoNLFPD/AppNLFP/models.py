from django.db import models

# Create your models here.
class Estadio(models.Model):
    nombreEstadio = models.CharField(max_length=30)
    capacidadEstadio = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombreEstadio


class Equipo(models.Model):
    nombreEquipo = models.CharField(max_length=30)
    colorEquipo = models.CharField(max_length=30)
    estadio = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombreEquipo

class Jugador(models.Model):
    nombreJugador = models.CharField(max_length=30)
    numeroJugador = models.IntegerField()
    equipo = models.CharField(max_length=30)
    posicion = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombreJugador


