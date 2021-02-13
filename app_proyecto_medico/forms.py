from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
import datetime

class FormularioLogin(forms.Form):
    email = forms.CharField(validators=[
        validators.MinLengthValidator(3, "El email debe contener mas de 3 caracteres")
    ])

    password = forms.CharField(validators=[
        validators.MinLengthValidator(5, "El password debe contener almenos 5 digitos")
    ])
    
class FormularioRegistro(forms.Form):
    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(3, "El nombre debe contener almenos 3 carateres")
    ])
    rut = forms.CharField(validators=[
        validators.MaxLengthValidator(9, "El rut debe contener al menos 9 caracteres")
    ])
    email = forms.CharField(validators=[
        validators.MinLengthValidator(3, "El email debe contener mas de 3 caracteres")
    ])

    password = forms.CharField(validators=[
        validators.MinLengthValidator(5, "El password debe contener almenos 5 digitos")
    ])

class FormularioExamen(forms.Form):
    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(3, "El nombre debe contener almenos 3 carateres")
    ])
    rut = forms.CharField(validators=[
        validators.MaxLengthValidator(9, "El rut debe contener al menos 9 caracteres")
    ])
    examen = forms.CharField(validators=[
        validators.MinLengthValidator(3, "El nombre del examen debe contener almenos 3 caracteres")
    ])

    medico = forms.CharField(validators=[
        validators.MinLengthValidator(1, "El nombre del medico debe contener almenos una letra")
    ])

def validar_fecha(fecha):
    fecha_menor = datetime.datetime.strptime("1800-01-01", "%Y-%m-%d").date()
    fecha_mayor = datetime.datetime.strptime("2021-12-31", "%Y-%m-%d").date()
    if fecha_menor <= fecha <= fecha_mayor:
        return fecha
    else:
        raise ValidationError("Sólo acepta fechas de diciembre 2020")

class FormularioPaciente(forms.Form):
    nombre = forms.CharField(
                validators = [ 
                        validators.MinLengthValidator( 3, 
						    "La marca no puede ser de menos de 3 letras"),
                        validators.MaxLengthValidator( 10, 
						    "La marca no puede ser de más de 10 letras") ])   
    sexo = forms.CharField(
                validators = [ 
                        validators.MinLengthValidator( 3, 
						    "El modelo no puede ser de menos de 3 letras"),
                        validators.MaxLengthValidator( 30, 
						    "El modelo no puede ser de más de 30 letras") ])
    edad = forms.IntegerField(validators = [ 
                        validators.MinValueValidator( 1, 
						    "No pueden ser menor de 1 año"),
                        validators.MaxValueValidator( 100, 
						    "No pueden ser más de 100 años") ])
    fecha_nacimiento = forms.DateField(validators = [validar_fecha])