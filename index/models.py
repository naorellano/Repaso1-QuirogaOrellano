from django.db import models

# Create your models here.

class futbolista(models.model):
    nombre = models.CharField(max_length=20)
    apellido = models.charfield(max_lenght=30)
    delantero = models.BooleanField()
    
    
    class basquetbolista:
        nombre = models.CharField(max_lenght=20)
        apellido = models.CharField(max_length=30)
        federado = models.BooleanField()
        
        