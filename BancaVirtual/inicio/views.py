from django.shortcuts import render

# Create your views here.
def login(request):
	return render(request,'login.html')

def cuentas(request):
	return render(request,'cuentas.html')

def monetaria(request):
	return render(request,'monetaria.html')