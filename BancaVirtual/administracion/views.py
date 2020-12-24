from django.shortcuts import render
from .forms import *
import MySQLdb
# Create your views here.



def crearClienteIndividual(request):
	form = clienteindividual()
	nombre = "Crear Cliente nuevo"
	variables = {
		"form":form,
		"mensaje": nombre
	}
	if request.method == "POST":
		form = clienteindividual(data=request.POST)
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

			nombre = "Cliente registrado de manera correcta"

			form = clienteindividual()
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
	nombre = "Crear Cliente nuevo"
	variables = {
		"form":form,
		"mensaje": nombre
	}
	if request.method == "POST":
		form = clienteindividual(data=request.POST)
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

			nombre = "Cliente registrado de manera correcta"

			form = clienteindividual()
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