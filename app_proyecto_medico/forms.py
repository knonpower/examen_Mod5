from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

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
    
