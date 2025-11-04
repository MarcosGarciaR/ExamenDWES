from django.shortcuts import render
from .models import *
from django.db.models import Avg, Max, Min, Q, Prefetch
from django.views.defaults import page_not_found


# Create your views here.

def index(request):
    return render(request, 'index.html') 

def ver_videojuego_fantasy(request, titulo, pais):
    videojuegos = Videojuego.objects.select_related('estudio_desarrollo').prefetch_related('estudio_desarrollo__estudio_sede').prefetch_related('plataforma') .filter(titulo__contains=titulo, estudio_desarrollo__estudio_sede__pais__contains=pais).all()
    
    return render(request, 'URLs/videojuegos_tituloYpais.html', {'lista_videojuegos':videojuegos})


"""
FROM 
    videojuego V
INNER JOIN 
    estudio E ON V.estudio_desarrollo_id = E.id
INNER JOIN 
    sede S ON E.id = S.estudio_id
LEFT JOIN 
    videojuego_plataformas VP ON V.id = VP.videojuego_id
LEFT JOIN
    plataforma P ON VP.plataforma_id = P.id
LEFT JOIN
    analisis A ON V.id = A.videojuego_id
"""

#   PÁGINAS DE ERRORES
def mi_error_404(request, exception=None):
    return render(request, 'Errores/404.html',None,None,404)

def mi_error_400(request, exception=None):
    return render(request, 'Errores/400.html',None,None,400)

def mi_error_403(request, exception=None):
    return render(request, 'Errores/403.html',None,None,403)

def mi_error_500(request, exception=None):
    return render(request, 'Errores/500.html',None,None,500)