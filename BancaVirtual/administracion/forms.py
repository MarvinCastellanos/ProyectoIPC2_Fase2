from django import forms
#from .models import *

class clienteempresarial(forms.Form):
	nit = forms.IntegerField(required = True, help_text='')
	tipoEmpresa = forms.IntegerField(required = True)
	nombreEmpresa = forms.CharField(required = True)
	nombreComercial = forms.CharField(required = True)
	dpiRepresentante = forms.CharField(required = True)
	nombreRepersentante = forms.CharField(required = True)
	apellidoRepersentante = forms.CharField(required = True)
	contrasena = forms.CharField(widget=forms.PasswordInput, required=True)

	class Meta:
        #model = Clienteindividual
		fields = ("cui","tipoEmpresa","nombreEmpresa","nombreComercial","dpiRepresentante","nombreRepersentante","apellidoRepersentante","contrasena")

class Clienteindividual(forms.Form):
	cui=forms.IntegerField(required=True)
	nit=forms.IntegerField(required=True)
	primerNombre=forms.CharField(required=True)
	segundoNombre=forms.CharField(required=True)
	primerApellido=forms.IntegerField(required=True)
	segundoApellido=forms.CharField(required=True)
	fechaNacimiento=forms.DateField(required=True)
	password= forms.CharField(widget=forms.PasswordInput, required=True)

	class Meta:
		fields=("nit","tipoEmpresa","nombreEmpresa","nombreComercial","dpiRepresentante","nombreRepersentante","apellidoRepersentante")
			
class cuenta(forms.Form):	
	cliente=forms.IntegerField(required=True)
	tipoCuenta=forms.IntegerField(required=True)
	saldo=forms.IntegerField(required=True)
	chequeAU_activo=forms.BooleanField(required=True)
	cuentaSuspendida=forms.BooleanField(required=True)

	class Meta:
		fields = ("cliente","tipoCuenta","saldo","chequeAU_activo","cuentaSuspendida")	

class retiro(forms.Form):
	noCuenta=forms.IntegerField(required=True)
	monto=forms.IntegerField(required=True)

	class Meta:
		fields=("noCuenta","monto")

class deposito(forms.Form):
	noCuenta=forms.IntegerField(required=True)
	monto=forms.IntegerField(required=True)

	class Meta:
		fields= ("noCuenta","monto")

class chequera(forms.Form):
	noCuenta=forms.IntegerField(required=True)

	class Meta:
		fields=("noCuenta")


#class producto2(forms.Form):
#    cui = forms.IntegerField(required = True, help_text='Campo numerico, ingrese solo digitos')
#    nit = forms.IntegerField(max_length=50, help_text='Nombre del producto',required = True)
#    class Meta:
#        fields = ("idproducto","nombre")