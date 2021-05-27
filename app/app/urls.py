"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#from django.views.generic import TemplateView
from users.views import ListadoUsuarios, DetalleUsuario, CrearUsuario, ActualizarUsuario, EliminarUsuario#, VerConexionUsuario
#from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # La ruta 'leer' en donde listamos todos los registros o postres de la Base de Datos
    path('users/', ListadoUsuarios.as_view(template_name = "users/index.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro 
    path('users/detalle/<int:pk>', DetalleUsuario.as_view(template_name = "users/detalles.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro  
    path('users/crear', CrearUsuario.as_view(template_name = "users/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos 
    path('users/editar/<int:pk>', ActualizarUsuario.as_view(template_name = "users/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos 
    path('users/eliminar/<int:pk>', EliminarUsuario.as_view(), name='eliminar'),  

    # La ruta 'ver' usarios conectados a un usuario dado
   path('users/conexiones/<int:pk>', DetalleUsuario.as_view(template_name = "users/conexion.html"), name='conexion'),
]
