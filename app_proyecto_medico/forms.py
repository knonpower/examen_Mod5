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
        validators.MinLengthValidator(9, "El rut debe contener al menos 9 caracteres")
    ])
    email = forms.CharField(validators=[
        validators.MaxLengthValidator(30, "El rut debe contener al menos 9 caracteres")
    ])
    hemograma = forms.CharField(validators=[
        validators.MaxLengthValidator(9, "El rut debe contener al menos 9 caracteres")
    ])
    orina = forms.CharField(validators=[
        validators.MinLengthValidator(1, "Debe ingresar examen de orina ")
    ])
    colesterol = forms.CharField(validators=[
        validators.MinLengthValidator(1, "Debe ingresar examen de colesterol ")
    ])
    examen = forms.CharField(validators=[
        validators.MinLengthValidator(3, "El nombre del examen debe contener almenos 3 caracteres")
    ])
    medico = forms.CharField(validators=[
        validators.MinLengthValidator(3, "El nombre del medico debe contener almenos 3 letras")
    ])
    fecha = forms.DateTimeField()

    resumen = forms.CharField(validators=[
        validators.MinLengthValidator(1, "Debe ingresa el resumen del examen")
    ])
    
