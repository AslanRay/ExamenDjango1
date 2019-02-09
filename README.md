# CESUN UNIVERSIDAD
#### Dirección academica
#### Ingeniería en Desarrollo de Software
#### Optativa II
----
##### Profesor Ray Brunett Parra Galaviz
##### **Alumno: RAYMUNDO LEÓN VIERA**
##### Matricula: MRIM11002
----
###  Intrucciones I: Leer detalladamente los reactivos y responder de manera correcta lo solicitado en los reactivos.
-----
##### 1. Dibuje un árbol con la estructura básica de un proyecto y una aplicación en Django
---
```
Proyecto
    ├── App
    │   ├── admin.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── manage.py
    └── Proyecto
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-36.pyc
        │   └── settings.cpython-36.pyc
        ├── settings.py
        ├── urls.py
        └── wsgi.py

```
##### 2. Mencione tres argumentos que gestiona el comando manage.py
---
```
makemigratios: para crear nuevas migraciones basadas en los cambios detecados en los modelos.
migrate: sincroniza el estado de la base de datos con el conjunto actual de modelos y migraciones
runserver: inicializa un servidor web ligero en la maquina local
shell: inicializa un interprete interactivo de python
```

##### 3. Explique la diferencia entre utilizar urls global y urls local
---
```
Las urls globales tienen como alcance todo el proyecto mientras que las urls locales solo la carpeta/app que las contiene
```

##### 4. Escriba un patrón de url para una vista basada en función
-----
```
path('lista-pokemon/', views.lista,name="lista"),
```
##### 5. Escriba un patrón de url para una vista basada en clase
-----
```
path('lista-pokemon/', views.ListaPokemon.as_view(),name="lista"),
```
##### 6. Escriba el comando para hacer un proyecto en Django
-----
```
django-admin.py startproject nombredelproyecto
```
##### 7. Escriba el comando para hacer una aplicación en Django
-----
```
python manage.py startapp nombredelaapp
```
##### 8. Mencione para que sirve el archivo Settings.py
-----
```
Para manejar las configuraciones del servidor, por ejemplo, los host/dominios que Django puede servir, las configuraciones para la base de datos; por defecto sqlite, instalar aplicaciones, definir donde podemos encontrar archivos estaticos, entre otras configuraciones.
```
##### 9. Escriba el comando para registrar las migraciones de los modelos
-----
```
python manage.py makemigrations
```
##### 10. Escriba el comando para sincronizar el modelo con el motor de base de datos
-----
```
python manage.py migrate
```
### Instrucciones II: Leer detalladamente la problemática y desarrollar un proyecto en Python y Django para solucionar la problemática establecida.
##### En la ciudad Parra’s existe la National League Football Parra (NLFP), esta liga esta solicitando a las casas desarrolladoras un proyecto a medida para registrar y controlar las estadísticas de la liga. La NLFP esta interesara en tener los siguientes reportes:
* Lista general de jugadores
* Lista general de equipos
* Lista general de estadios
* Detalle de jugadores
* Detalle de estadios
* Detalle de equipos
* Lista de jugadores de un equipo proporcionado por el usuario
* Lista de todos los jugadores de una posicion especificda por el usuario

#### Importante: Realizar las vistas, modelos, urls, formas y demás cosas necesarias para cumplir con la necesidad de los reportes. Los reportes deben obtener su información mediante un queryset al modelo.
