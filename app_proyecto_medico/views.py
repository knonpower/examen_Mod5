from django.shortcuts import render, redirect
from django.conf import settings
from .forms import FormularioLogin
from .forms import FormularioRegistro
from .forms import FormularioExamen
from .forms import FormularioPaciente

import datetime
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
        filename = "/app_proyecto_medico/data/examen.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            data = json.load(file)
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

        filename = '/app_proyecto_medico/data/examen.json'
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            data = json.load(file)
        for paciente in data['formulario']:
            if int(paciente['identificador']) == int(id):
                print(paciente['nombre'], paciente['rut'])
                perfil = {'perfil': paciente}
                print("Estos son los datos del paciente: ", paciente)

        context = {'lista_paciente': data['formulario']}
        context.update(perfil)
        print("El context con update tiene:", context)
        return render(request, 'app_proyecto_medico/privada.html', context)


def graficos(request):
    lista_examen = []
    lista_medico = []
    filename = "/app_proyecto_medico/data/examen.json"
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        lista_pacientes = json.load(file)
        for elemento in lista_pacientes.get('formulario')[-5:]:
            examen = elemento.get('examen')
            medico = elemento.get('medico')
            lista_examen.append(examen)
            lista_medico.append(medico)
    print(lista_examen)
    print(lista_medico)
    context = {'examen': lista_examen, 'medico': lista_medico}
    return render(request, 'app_proyecto_medico/graficos.html', context)


def context_lista_examen():
    filename = "/app_proyecto_medico/data/examen.json"
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        formulario = json.load(file)
    context = {'lista_examen': formulario['formulario']}
    return context


def examenes(request):
    if request.method == "GET":
        formulario = FormularioExamen()
        context = {'formulario': formulario}
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
                data = json.load(file)
                nuevo_ultimo_identificador = int(
                    data['ultimo_identificador'])+1
                data['ultimo_identificador'] = nuevo_ultimo_identificador
                datos_formulario['identificador'] = nuevo_ultimo_identificador
                data['formulario'].append(datos_formulario)
            with open(str(settings.BASE_DIR)+filename, 'w') as file:
                json.dump(data, file)
            return redirect('app_proyecto_medico:examenes')
        else:
            context = {'formulario': formulario_devuelto}
            return render(request, 'app_proyecto_medico/examenes.html', context)


def lista_examen(request):
    context = context_lista_examen()
    return render(request, 'app_proyecto_medico/examen.html', context)


def agendar(request):
    return render(request, 'app_proyecto_medico/agendar.html')


def registro(request):
    if request.method == "GET":
        formulario = FormularioRegistro()
        context = {'formulario': formulario}
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
                data = json.load(file)
                nuevo_ultimo_identificador = int(
                    data['ultimo_identificador'])+1
                data['ultimo_identificador'] = nuevo_ultimo_identificador
                datos_formulario['identificador'] = nuevo_ultimo_identificador
                data['formulario'].append(datos_formulario)
            with open(str(settings.BASE_DIR)+filename, 'w') as file:
                json.dump(data, file)
            return redirect('app_proyecto_medico:login')
        else:
            context = {'formulario': formulario_devuelto}
            return render(request, 'app_proyecto_medico/registro.html', context)


def login(request):
    if request.method == "GET":
        formulario = FormularioLogin()
        context = {'formulario': formulario}
        print("El GET contiene", context)
        return render(request, 'app_proyecto_medico/login.html', context)

    elif request.method == "POST":
        print("El POST contiene:", request.POST)

        formulario_devuelto = FormularioLogin(request.POST)
        print("Este es el formulario devuelto: ", formulario_devuelto)
        if formulario_devuelto.is_valid() == True:

            datos_formulario = formulario_devuelto.cleaned_data

            print("Los datos limpios del formulario son:", datos_formulario)
            filename = "/app_proyecto_medico/data/login.json"
            with open(str(settings.BASE_DIR)+filename, 'r') as file:
                data = json.load(file)
                print("Esto es data", data)
            for form in datos_formulario:
                print("Primer for", form)
                for formulario in data['formulario']:
                    print("Segundo for")
                    print("Este es el json:", formulario)
                    print("Este es el formulario:", datos_formulario)
                    if datos_formulario['email'] == formulario['email'] and formulario['password'] == datos_formulario['password']:

                        print("El email si existe", datos_formulario)
                        return redirect('app_proyecto_medico:privada')
                    else:
                        print("El email no existe")
            context = {'formulario': formulario_devuelto}
            return render(request, 'app_proyecto_medico/login.html', context)
        else:
            context = {'formulario': formulario_devuelto}
            return render(request, 'app_proyecto_medico/login.html', context)


def context_lista_pacientes():
    filename = "/app_proyecto_medico/data/pacientes.json"
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        pacientes = json.load(file)
    context = {'lista_paciente': pacientes['paciente']}
    return context


def crear_paciente(request):
    if request.method == "GET":
        formulario = FormularioPaciente()
        context = {'formulario': formulario}
        context.update(context_lista_pacientes())
        print(context)
        return render(request, 'app_proyecto_medico/crear_paciente.html', context)

    elif request.method == "POST":
        print("El POST contiene:", request.POST)

        formulario_devuelto = FormularioPaciente(request.POST)

        if formulario_devuelto.is_valid() == True:
            datos_formulario = formulario_devuelto.cleaned_data
            datos_formulario['fecha_nacimiento'] = datos_formulario['fecha_nacimiento'].strftime(
                "%Y-%m-%d")
            print("Los datos limpios del formulario son:", datos_formulario)
            filename = "/app_proyecto_medico/data/pacientes.json"
            with open(str(settings.BASE_DIR)+filename, 'r') as file:
                data = json.load(file)
                nuevo_ultimo_identificador = int(
                    data['ultimo_identificador']) + 1
                data['ultimo_identificador'] = nuevo_ultimo_identificador
                datos_formulario['identificador'] = nuevo_ultimo_identificador
                data['paciente'].append(datos_formulario)
            with open(str(settings.BASE_DIR)+filename, 'w') as file:
                json.dump(data, file)

            return redirect('app_proyecto_medico:crear_paciente')
        else:
            context = {'formulario': formulario_devuelto}
            context.update(context_lista_pacientes())
            return render(request, 'app_proyecto_medico/crear_paciente.html', context)


def lista_paciente(request):
    context = context_lista_pacientes()
    print("este es el context de lista pacientes", context)
    return render(request, 'app_proyecto_medico/lista_paciente.html', context)


def eliminar_paciente(request, identificador):
    if request.method == "GET":
        context = {'identificador': identificador}
        return render(request, "app_proyecto_medico/eliminar_paciente.html", context)

    if request.method == "POST":
        filename = "/app_proyecto_medico/data/pacientes.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            data = json.load(file)
        for formulario in data['paciente']:
            if int(formulario['identificador']) == int(identificador):
                data['paciente'].remove(formulario)
                break
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(data, file)

        return redirect('app_proyecto_medico:lista_paciente')

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