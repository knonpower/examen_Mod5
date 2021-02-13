from django.urls import path
from . import views

app_name = "app_proyecto_medico"

urlpatterns = [
    path('', views.index, name='index'),
    path('privada', views.privada, name='privada'),
    path('graficos', views.graficos, name='graficos'),
    path('examenes', views.examenes, name='examenes'),
    path('agendar', views.agendar, name='agendar'),
    path('login', views.login, name='login'),
    path('registro', views.registro, name='registro'),
    path('crear_paciente', views.crear_paciente, name='crear_paciente'),
    path('lista_paciente', views.lista_paciente, name='lista_paciente'),
    path('<identificador>/eliminar_paciente', views.eliminar_paciente, name='eliminar_paciente'),
    
]