from django.shortcuts import render, redirect
from django.conf import settings
from .forms import FormularioLogin
from .forms import FormularioRegistro
from .forms import FormularioExamen

from django.utils.datastructures import MultiValueDictKeyError

import json





# Create your views here.

def index(request):
    return render(request, 'app_proyecto_medico/index.html')

def privada(request):
    if request.method == "GET":
        print("El request GET: ", request.GET)
        if 'id' in request.GET:
            id = request.GET['id']
            print("El id del GET es: ", id)
        filename="/app_proyecto_medico/data/examen.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            data=json.load(file)
            #print("Esto es data", data)
        for paciente in data['formulario']:
            cliente = paciente['nombre'], paciente['identificador']
            #print("el cliente tiene:",  cliente)
        
        context = {'lista_paciente': data['formulario']}
        
        print("El context contiene", context)
        return render(request, 'app_proyecto_medico/privada.html', context)


    elif request.method == "POST":
        print("El request GET: ", request.GET)
        if 'id' in request.GET:
            id = request.GET['id']
            print("El id en el GET es: ", id)

        filename ='/app_proyecto_medico/data/examen.json'
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            data=json.load(file)
        for paciente in data['formulario']:
            if int(paciente['identificador']) == int(id):
                print(paciente['nombre'], paciente['rut'])
                perfil = {'perfil': paciente}
                print("Estos son los datos del paciente: ",paciente)
            
        context = {'lista_paciente': data['formulario']}
        context.update(perfil)   
        print("El context con update tiene:",context)     
        return render(request, 'app_proyecto_medico/privada.html', context)


def graficos(request):
    return render(request, 'app_proyecto_medico/graficos.html')

def context_lista_examen():
    filename= "/app_proyecto_medico/data/examen.json"
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        formulario=json.load(file)
    context = {'lista_examen': formulario['formulario']}
    return context
    
def lista_examen(request):
    context = context_lista_examen()
    return render(request, 'app_proyecto_medico/examenes.html', context)

def examenes(request):
    if request.method == "GET":
        formulario = FormularioExamen()
        context = {'formulario':formulario}
        context.update(context_lista_examen())
        print("El GET de examenes contiene", context)
        
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

def eliminar_examen(request, identificador):
    if request.method == 'GET':
        context ={'identificador':identificador}
        return render(request, 'app_proyecto_medico/eliminar_examen.html', context)
    
    if request.method == 'POST':
        filename ='/app_proyecto_medico/data/examen.json'
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            data=json.load(file)
        for formulario in data['formulario']:
            if int(formulario['identificador']) == int(identificador):
                data['formulario'].remove(formulario)
                break
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(data, file)
        return redirect('app_proyecto_medico:examenes')

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