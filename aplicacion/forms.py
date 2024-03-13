from django import forms

class InstitucionForm(forms.Form):
    nombre = forms.CharField(max_length=60, required=True)
    direccion = forms.CharField(max_length=60, required=True) #CharField si queremos ingresar un texto #IntegerField para que sea numerico
    

class PosicionForm(forms.Form):
    equipo = forms.CharField(max_length=60, required=True)
    puntos = forms.IntegerField(required=True)
    
class TablaGoleadoresForm(forms.Form):
    jugador = forms.CharField(max_length=60, required=True)
    goles = forms.IntegerField(required=True)
    
    

