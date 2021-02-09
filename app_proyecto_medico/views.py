from django.shortcuts import render, redirect
from django.conf import settings
from .forms import FormularioLogin
from .forms import FormularioRegistro

import json

# Create your views here.

def index(request):
    return render(request, 'app_proyecto_medico/index.html')

def privada(request):
    return render(request, 'app_proyecto_medico/privada.html')

def graficos(request):
    return render(request, 'app_proyecto_medico/graficos.html')

def examenes(request):
    return render(request, 'app_proyecto_medico/examenes.html')

def agendar(request):
    return render(request, 'app_proyecto_medico/agendar.html')

def registro(request):
    if request.method == "GET":
        formulario = FormularioRegistro()
        context = {'formulario':formulario}
        print("El GET contiene", context)
        return render(request, 'app_proyecto_medico/registro.html', context)

def login(request):
    if request.method == "GET":
        formulario = FormularioLogin()
        context = {'formulario':formulario}
        print("El GET contiene", context)
        return render(request, 'app_proyecto_medico/login.html', context)

    elif request.method == "POST":
        print("El POST contiene:", request.POST)

        formulario_devuelto = FormularioLogin(request.POST)
        print("Este es el formulario devuelto: ",formulario_devuelto)
        if formulario_devuelto.is_valid() == True:
            
            datos_formulario = formulario_devuelto.cleaned_data
            
            print("Los datos limpios del formulario son:", datos_formulario)
            filename="/app_proyecto_medico/data/login.json"
            with open(str(settings.BASE_DIR)+filename, 'r') as file:
                data=json.load(file)
                print("Esto es data",data)
            for form in datos_formulario:
                print("Primer for", form)
                for  formulario in data['formulario']:
                    print("Segundo for")
                    print("Este es el json:", formulario)
                    print("Este es el formulario:", datos_formulario)
                    if datos_formulario['email'] == formulario['email'] and formulario['password'] == datos_formulario['password']:
                        
                        print("El email si existe", datos_formulario)
                        return redirect('app_proyecto_medico:privada') 
                    else:
                        print("El email no existe")
            context ={'formulario':formulario_devuelto}
            return render(request, 'app_proyecto_medico/login.html', context)
            
            """  
            for formulario in data['formulario']:
                print("Este es el json:",formulario)
                print("Este es el formulario:", datos_formulario)
                email = formulario['email']
                print(email)

                if datos_formulario['email'] in formulario['email']:
                    print("El email existe:",email)
                    verdadero = True
                if datos_formulario['email'] is not formulario['email']:
                    print("El email no existe")
                    verdadero = False 
                    context ={'formulario':formulario_devuelto}
                    return render(request, 'app_proyecto_medico/login.html', context)   
                if formulario['email'] == datos_formulario['email'] and formulario['password'] == datos_formulario['password']:
                    return redirect('app_proyecto_medico:privada')
                else:
                    return render(request, 'app_proyecto_medico/index.html')
                """
        else:
            context ={'formulario':formulario_devuelto}
            return render(request, 'app_proyecto_medico/login.html', context)