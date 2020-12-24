from django import forms

class cuenta(forms.Form):	
	cliente=forms.IntegerField(required=True)
	tipoCuenta=forms.IntegerField(required=True)
	saldo=forms.IntegerField(required=True)
	chequeAU_activo=forms.BooleanField(required=True)
	cuentaSuspendida=forms.BooleanField(required=True)

	class Meta:
		fields = ("cliente"."tipoCuenta","saldo","chequeAU_activo","cuentaSuspendida")	