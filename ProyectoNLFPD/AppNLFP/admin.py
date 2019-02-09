from django.contrib import admin
from .models import Estadio
from .models import Equipo
from .models import Jugador
# Register your models here.

admin.site.register(Estadio)
admin.site.register(Equipo)
admin.site.register(Jugador)