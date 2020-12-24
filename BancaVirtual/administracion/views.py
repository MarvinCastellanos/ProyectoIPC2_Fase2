from django.shortcuts import render
from .forms import *
import MySQLdb
# Create your views here.



def crearClienteIndividual(request):
	form = Clienteindividual()
	nombre = "Crear Cliente nuevo"
	variables = {
		"form":form,
		"mensaje": nombre
	}
	if request.method == "POST":
		form = Clienteindividual(data=request.POST)
		if form.is_valid():
			datos = form.cleaned_data

			cui = datos.get("cui")
			nit = datos.get("nit")
			primernombre = datos.get("primernombre")
			segundonombre = datos.get("segundonombre")
			primerapellido = datos.get("primerapellido")
			segundoapellido = datos.get("segundoapellido")
			fechanacimiento = datos.get("fechanacimiento")
			password= datos.get("contra")

			host = 'localhost'
			db_name = 'bancaVirtual'
			user = 'root'
			contra = 'Ca$tellanos333'
			puerto = 3306

			db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
			c = db.cursor()
			consulta = "INSERT INTO clienteIndividual VALUES("+str(cui)+","+str(nit)+",'"+primernombre+"','"+segundonombre+"','"+primerapellido+"','"+segundoapellido+"','"+str(fechanacimiento)+"');"
			c.execute(consulta)

			consulta = "INSERT INTO cliente(clienteIndividual,password) VALUES("+str(cui)+",'"+password+"');"
			c.execute(consulta)
			db.commit()
			c.close()

			#nombre = "Cliente registrado de manera correcta"

			form = Clienteindividual()
			variables = {
			"form": form,
			"mensaje": nombre
			}
		else:
			nombre= "Cliente ya registrado"
		variables = {
        	"form":form,
        	"mensaje":nombre
        }

	return render(request,'administracion/crearCliente.html',variables)

def crearClienteEmpresarial(request):
	form = clienteempresarial()
	nombre = "Crear Cliente Empresarial"
	variables = {
		"form":form,
		"mensaje": nombre
	}
	if request.method == "POST":
		form = clienteempresarial(data=request.POST)
		if form.is_valid():
			datos = form.cleaned_data

			
			nit = datos.get("nit")
			tipoEmpresa = datos.get("tipoEmpresa")
			nombreEmpresa = datos.get("nombreEmpresa")
			nombreComercial = datos.get("nombreComercial")
			dpiRepresentante = datos.get("dpiRepresentante")
			nombreRepersentante = datos.get("nombreRepersentante")
			apellidoRepersentante = datos.get("apellidoRepersentante")
			contrasena= datos.get("contrasena")

			host = 'localhost'
			db_name = 'bancaVirtual'
			user = 'root'
			contra = 'Ca$tellanos333'
			puerto = 3306

			db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
			c = db.cursor()
			consulta = "INSERT INTO clienteEmpresarial VALUES("+str(nit)+","+str(tipoEmpresa)+",'"+nombreEmpresa+"','"+nombreComercial+"','"+dpiRepresentante+"','"+nombreRepersentante+"','"+contrasena+"');"
			c.execute(consulta)

			consulta = "INSERT INTO cliente(clienteEmpresarial,password) VALUES("+str(nit)+",'"+contrasena+"');"
			c.execute(consulta)
			db.commit()
			c.close()

			#nombre = "Cliente registrado de manera correcta"

			form = clienteempresarial()
			variables = {
			"form": form,
			"mensaje": nombre
			}
		else:
			nombre= "Cliente ya registrado"
		variables = {
        	"form":form,
        	"mensaje":nombre
        }

	return render(request,'administracion/creaClienteEmpresarial.html',variables)

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