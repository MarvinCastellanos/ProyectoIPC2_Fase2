from django.shortcuts import render

# Create your views here.
def crearCliente(request):
	return render(request,'administracion/crearCliente.html')

def crearCuenta(request):
	return render(request,'administracion/crearCuenta.html')

def cobraCheque(request):
	return render(request,'administracion/cobraCheque.html')

def creaChequera(request):
	return render(request,'administracion/creaChequera.html')

def deposito(request):
	return render(request,'administracion/deposito.html')

def credito(request):
	return render(request,'administracion/credito.html')

def desbloquea(request):
	return render(request,'administracion/desbloqueo.html')