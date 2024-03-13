from django.db import models

# Create your models here.

class Institucion(models.Model):
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
        
    def __str__(self):
        return f"{self.nombre}, {self.direccion}"
    
    class Meta:
        verbose_name = "Institucion"
        verbose_name_plural ="Institucion"
        ordering = ["nombre"]

class TablaGoleadores(models.Model):
    jugador = models.CharField(max_length=60)
    goles = models.PositiveIntegerField(default=0)
        
    def __str__(self):
        return f"{self.jugador}, {self.goles}"
    
    class Meta:
        verbose_name = "TablaGoleadores"
        verbose_name_plural ="TablaGoleadores"
        ordering = ["jugador"]
    
class Posicion(models.Model):
    equipo = models.CharField(max_length=60)
    puntos = models.IntegerField(default=0)
        
    def __str__(self):
        return f"{self.equipo}, {self.puntos}"
    
    class Meta:
        verbose_name = "Posicion"
        verbose_name_plural ="Posicion"
        ordering = ["equipo"]