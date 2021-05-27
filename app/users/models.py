from django.db import models

from django.utils import timezone
 
# Creación de campos de la tabla 'users' 
class Connections(models.Model):
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    connection = models.CharField(max_length=100, default='DEFAULT VALUE')
   
    class Meta:
         db_table = 'connections' # Le doy de nombre 'postres' a nuestra tabla en la Base de Datos

