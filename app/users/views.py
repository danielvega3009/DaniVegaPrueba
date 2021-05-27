from django.shortcuts import render

# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
# Instanciamos el modelo 'Connections' para poder usarlo en nuestras Vistas CRUD
from .models import Connections

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms

class ListadoUsuarios(ListView): 
    model = Connections
 
class DetalleUsuario(DetailView): 
    model = Connections
 
class CrearUsuario(SuccessMessageMixin, CreateView): 
    model = Connections
    form = Connections
    fields = "__all__" 
    success_message = 'Usuario Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Usuario     
 
    # Redireccionamos a la página principal luego de crear un registro o usuario
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer' 
 
class ActualizarUsuario(SuccessMessageMixin, UpdateView): 
    model = Connections
    form = Connections
    fields = "__all__"  
    success_message = 'Usuario Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Usuario 
 
    # Redireccionamos a la página principal luego de actualizar un registro o usuario
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer' 
 
class EliminarUsuario(SuccessMessageMixin, DeleteView): 
    model = Connections 
    form = Connections
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o usuario
    def get_success_url(self): 
        success_message = 'Usuario Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Usuario 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

#class VerConexionUsuario(ListView): 
   # model = Connections