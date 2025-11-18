from django.urls import path, re_path
from .import views

urlpatterns = [
    path('', views.index , name='index'),
    path('animal/<str:nombre>/refugio/<str:refugio>/', views.ejercicio1 , name='ejercicio1'),
    path('vacunas/<str:valor>', views.ejercicio2 , name='ejercicio2'),
    path('enlaceNone', views.ejercicio3 , name='ejercicio3'),
]