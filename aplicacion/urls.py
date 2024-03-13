from django.urls import path, include
from .views import *

#_menuprincipal

urlpatterns = [
    path('', home, name="home"),
    #__ posicion
    
    path('Posicion/', PosicionList.as_view(), name= "Posicion"),
    path("Posicion_create/", PosicionCreate.as_view(), name="Posicion_create"),
    path("Posicion_update/<int:pk>", PosicionUpdate.as_view(), name="Posicion_update"),
    path("Posicion_delete/<int:pk>", PosicionDelete.as_view(), name="Posicion_delete"),
    
    #__institucion
    
    path('institucion/', InstitucionList.as_view(), name="Institucion"),
    path('Institucion_create/', InstitucionCreate.as_view(), name="Institucion_create"),
    path("Institucion_update/<int:pk>", InstitucionUpdate.as_view(), name="Institucion_update"),
    path("Institucion_delete/<int:pk>", InstitucionDelete.as_view(), name="Institucion_delete"),
#__ tabla goleadores

    path('TablaGoleadores/', TablaGoleadoresList.as_view(), name="TablaGoleadores"),
    path("TablaGoleadores_create/", TablaGoleadoresCreate.as_view(), name="TablaGoleadores_create"),
    
    #_acerca de mi
    
    path('acerca/', acerca, name="acerca_de_mi"),
    path('buscar_institucion/', buscarInstitucion, name="buscar_institucion"),
    path('encontrar_Institucion/', encontrarInstitucion, name="encontrar_institucion"),
    path('buscar_posicion/', buscarPosicion, name="buscar_posicion"),
    path('encontrar_posicion/', encontrarPosicion, name="encontrar_posicion"),
    #___form
    
    path('institucion_form/', institucionForm, name="Institucion_form"),
    path('posicionForm/', posicionForm, name="Posicion_form"),
    path('TablaGoleadores_form/', TablaGoleadoresForm, name="TablaGoleadores_form"),
    
    ]