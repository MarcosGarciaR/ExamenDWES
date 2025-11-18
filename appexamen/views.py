from django.shortcuts import render
from .models import *
from django.db.models import Avg, Max, Min, Q, Prefetch
from django.views.defaults import page_not_found


# Create your views here.

def index(request):
    return render(request, 'index.html')


def ejercicio1(request, nombre, refugio):
    datos = (Animal.objects
                .select_related('centro__refugio')
                .filter(nombre__contains=nombre, centro__refugio__nombre=refugio)
                .all()
                )
    return render(request, 'URLs/ejercicio1.html', {'datos':datos })


def ejercicio2(request, valor):
    datos = (Animal.objects
                .prefetch_related(Prefetch("vacunas__animal_vacunas"))
                .prefetch_related("revisiones")
                .filter(Q(vacunas__fabricante=valor) | Q(vacunas__nombre__contains = valor), 
                        revisiones__puntuacion_salud__gt=80)
                [:3]
                .all()
                )
    return render(request, 'URLs/ejercicio2.html', {'datos':datos })

def ejercicio3(request):
    datos = (Animal.objects.
                prefetch_related('animal_vacunas').
                filter(vacunas__id=None)
                .all().order_by('edad_estimada').reverse())
    return render(request, 'URLs/ejercicio1.html', {'datos':datos})


def ejercicio4(request, annio):
    datos = (Refugio.objects
                .filter(centros__animales__revisiones__fecha__year = annio)
                .distinct().all()
                .order_by('centros__animales__edad_estimada').reverse()
                )
    return render(request, 'URLs/ejercicio4.html', {'datos':datos})

#   PÁGINAS DE ERRORES
def mi_error_404(request, exception=None):
    return render(request, 'Errores/404.html',None,None,404)

def mi_error_400(request, exception=None):
    return render(request, 'Errores/400.html',None,None,400)

def mi_error_403(request, exception=None):
    return render(request, 'Errores/403.html',None,None,403)

def mi_error_500(request, exception=None):
    return render(request, 'Errores/500.html',None,None,500)