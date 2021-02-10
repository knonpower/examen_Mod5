from django.shortcuts import render, redirect
from django.conf import settings
from .forms import FormularioLogin
from .forms import FormularioRegistro
from .forms import FormularioExamen

import json





# Create your views here.

def index(request):
    return render(request, 'app_proyecto_medico/index.html')

def privada(request):
    return render(request, 'app_proyecto_medico/privada.html')

def graficos(request):
    return render(request, 'app_proyecto_medico/graficos.html')

def examenes(request):
    if request.method == "GET":
        formulario = FormularioExamen()
        context = {'formulario':formulario}
        print("El GET contiene", context)
        return render(request, 'app_proyecto_medico/examenes.html', context)
    
    elif request.method == "POST":
        print("El POST contiene: ", request.POST)
        formulario_devuelto = FormularioExamen(request.POST)
        print("Este es el formulario devuelto: ", formulario_devuelto)
        
        if formulario_devuelto.is_valid() == True:
            datos_formulario = formulario_devuelto.cleaned_data
            print("Los datos limpios del formulario son: ", datos_formulario)
            filename = "/app_proyecto_medico/data/examen.json"
            with open(str(settings.BASE_DIR)+filename, 'r') as file:
                data=json.load(file)
                nuevo_ultimo_identificador = int(data['ultimo_identificador'])+1
                data['ultimo_identificador'] = nuevo_ultimo_identificador
                datos_formulario['identificador'] = nuevo_ultimo_identificador
                data['formulario'].append(datos_formulario)
            with open(str(settings.BASE_DIR)+filename, 'w') as file:
                json.dump(data, file)
            return redirect('app_proyecto_medico:examenes')
        else:
            context = {'formulario':formulario_devuelto}
            return render(request, 'app_proyecto_medico/examenes.html', context)


def lista_examen(request):
    filename= "/app_proyecto_medico/data/examen.json"
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        formulario=json.load(file)
    context = {'formulario':formulario}
    print("Lista examenes",context)
    return render(request, 'app_proyecto_medico/examenes.html', context)

def agendar(request):
    return render(request, 'app_proyecto_medico/agendar.html')

def registro(request):
    if request.method == "GET":
        formulario = FormularioRegistro()
        context = {'formulario':formulario}
        print("El GET contiene", context)
        return render(request, 'app_proyecto_medico/registro.html', context)
    
    elif request.method == "POST":
        print("El POST contiene: ", request.POST)

        formulario_devuelto = FormularioRegistro(request.POST)
        print("Este es el formulario devuelto: ", formulario_devuelto)

        if formulario_devuelto.is_valid() == True:
            datos_formulario = formulario_devuelto.cleaned_data
            print("Los datos limpios del formulario son: ", datos_formulario)
            filename = "/app_proyecto_medico/data/login.json"
            with open(str(settings.BASE_DIR)+filename, 'r') as file:
                data=json.load(file)
                nuevo_ultimo_identificador = int(data['ultimo_identificador'])+1
                data['ultimo_identificador'] = nuevo_ultimo_identificador
                datos_formulario['identificador'] = nuevo_ultimo_identificador
                data['formulario'].append(datos_formulario)
            with open(str(settings.BASE_DIR)+filename, 'w') as file:
                json.dump(data, file)
            return redirect('app_proyecto_medico:login')
        else:
            context = {'formulario':formulario_devuelto}
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
        else:
            context ={'formulario':formulario_devuelto}
            return render(request, 'app_proyecto_medico/login.html', context)