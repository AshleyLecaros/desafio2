from django.db import models

# Create your models here.

class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    eliminada = models.BooleanField(default=False) # Campo para marcar si la tarea esta eliminada (por defecto False)
    
class SubTarea(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    eliminada = models.BooleanField(default=False)
    tarea = models.ForeignKey(Tarea, related_name='subtareas', on_delete=models.CASCADE) #Llave foranea (modelo Tarea), con eliminación en cascada
    

