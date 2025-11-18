from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Refugio(models.Model):
    nombre = models.CharField(max_length=100)

class Centro(models.Model):
    nombre = models.CharField(max_length=100)
    refugio = models.ForeignKey(Refugio, on_delete=models.CASCADE, related_name='centros')

class Vacuna(models.Model):
    nombre = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE, related_name='animales')
    edad_estimada = models.IntegerField(null=True, blank=True)
    vacunas = models.ManyToManyField(Vacuna, related_name="animal_vacunas")

class Revision_Veterinaria(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='revisiones')
    puntuacion_salud = models.IntegerField()
    fecha = models.DateField()
    veterinario = models.CharField(max_length=150)
