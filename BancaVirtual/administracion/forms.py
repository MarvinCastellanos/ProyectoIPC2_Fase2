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

#class producto2(forms.Form):
#    cui = forms.IntegerField(required = True, help_text='Campo numerico, ingrese solo digitos')
#    nit = forms.IntegerField(max_length=50, help_text='Nombre del producto',required = True)
#    class Meta:
#        fields = ("idproducto","nombre")