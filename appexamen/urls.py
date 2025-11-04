from django.urls import path, re_path
from .import views

urlpatterns = [
    path('', views.index , name='index'),
    path('videojuegos/titulo/<str:titulo>/pais/<str:pais>/', views.ver_videojuego_fantasy, name='ver_videojuego_fantasy'),
    
]