"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
#Path de usuarios
    #path('',views.login),
    path('administracion/crearClienteIndividual/', views.crearClienteIndividual),
    path('administracion/crearClienteEmpresarial/', views.crearClienteEmpresarial),
    path('administracion/crearCuenta/', views.crearCuenta),
    path('administracion/cobrarCheque/', views.cobraCheque),
    path('administracion/crearChequera/', views.creaChequera),
    path('administracion/deposito/', views.deposito),
    path('administracion/credito/', views.credito),
    path('administracion/desbloquea/', views.desbloquea),
    
]