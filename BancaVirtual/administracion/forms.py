from django import forms
#from .models import *

class clienteindividual(forms.Form):
	cui = forms.IntegerField(required = True, help_text='')
	nit = forms.IntegerField(required = True)
	primernombre = forms.CharField(required = True)
	segundonombre = forms.CharField(required = True)
	primerapellido = forms.CharField(required = True)
	segundoapellido = forms.CharField(required = True)
	fechanacimiento = forms.DateField(required = True)
	contra = forms.CharField(widget=forms.PasswordInput, required=True)

	class Meta:
        #model = Clienteindividual
		fields = ("cui","nit","primernombre","segundonombre","primerapellido","segundoapellido","fechanacimiento","contra")

class clienteempresarial(forms.Form):
	nit=forms.IntegerField(required=True)
	tipoEmpresa=forms.IntegerField(required=True)
	nombreEmpresa=forms.CharField(required=True)
	nombreComercial=forms.CharField(required=True)
	dpiRepresentante=forms.IntegerField(required=True)
	nombreRepersentante=forms.CharField(required=True)
	apellidoRepersentante=forms.CharField(required=True)

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