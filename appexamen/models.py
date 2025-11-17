from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


"""
# ESTUDIO
class Estudio(models.Model):
    nombre = models.CharField(max_length=100)

# PLATAFORMA
class Plataforma(models.Model):
    OPCIONES_FAB = [
        ('sony', 'Sony'),
        ('ea', 'Electronic Arts')
    ]
    OPCIONES_NOM = [
        ('play','Play Station'),
        ('xbox','Xbox')
    ]
    nombre = models.CharField(max_length=100, choices=OPCIONES_NOM)
    fabricante = models.CharField(max_length=100, choices=OPCIONES_FAB)

# SEDE
class Sede(models.Model):
    OPCIONES_PAIS = [
        ('SP', 'España'),
        ('EEUU', 'Estados Unidos')
    ]
    estudio = models.OneToOneField(Estudio, on_delete=models.CASCADE, related_name="estudio_sede")
    pais = models.CharField(max_length= 50, choices=OPCIONES_PAIS)


# VIDEOJUEGO
class Videojuego(models.Model):
    titulo = models.CharField(max_length=150)
    ventas_estimadas = models.IntegerField(validators=[MinValueValidator(1)])
    estudio_desarrollo = models.ForeignKey(Estudio, on_delete=models.PROTECT)
    plataforma = models.ManyToManyField(Plataforma, related_name="videojuego_plataformas")

# ANALISIS
class Analisis(models.Model):
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE, related_name='analisisDeVideojuego')
    puntuacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    
"""