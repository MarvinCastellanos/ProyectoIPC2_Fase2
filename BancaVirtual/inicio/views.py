from django.shortcuts import render

# Create your views here.
#********************************************************
#views de usuario
#********************************************************
def login(request):
	return render(request,'user/login.html')

def cuentas(request):
	return render(request,'user/cuentas.html')

#def monetaria(request):
	#return render(request,'monetaria.html')

def transaccionPropia(request):
	return render(request,'user/transaccionPropia.html')

def transaccionTercero(request):
	return render(request,'user/transaccionTercero.html')

def suspende(request):
	return render(request,'user/suspende.html')

def autorizaCheque(request):
	return render(request,'user/autorizaCheque.html')

def estadoCuenta(request):
	return render(request,'user/estadoCuenta.html')

def chequera(request):
	return render(request,'user/chequera.html')

