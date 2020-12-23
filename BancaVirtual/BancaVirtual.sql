#drop database bancaVirtual;
create database bancaVirtual;
use bancaVirtual;

create table tipoEmpresa(
id int auto_increment primary key,
descripcion varchar(30) not null
);

create table clienteEmpresarial(
nit bigint primary key,
tipoEmpresa int not null,
nombreEmpresa varchar(30) not null,
nombreComercial varchar(30) not null,
dpiRepresentante varchar(20) not null,
nombreRepersentante varchar(30) not null,
apellidoRepersentante varchar(30) not null,
foreign key(tipoEmpresa) references tipoEmpresa(id)
);

create table clienteIndividual(
cui bigint primary key,
nit bigint not null,
primerNombre varchar(30) not null,
segundoNombre varchar(30) not null,
primerApellido varchar(30) not null,
segundoApellido varchar(30) not null,
fechaNacimiento date not null
);

create table cliente(
id int primary key auto_increment,
clienteIndividual bigint,
clienteEmpresarial bigint,
password varchar(30) not null,
foreign key(clienteIndividual) references clienteIndividual(cui),
foreign key(clienteEmpresarial) references clienteEmpresarial(nit)
);

create table tipoCuenta(
id int primary key auto_increment,
descripcion varchar(30) not null
);

create table cuenta(
numeroCuenta bigint primary key auto_increment,
cliente int not null,
tipoCuenta int not null,
saldo int not null,
chequeAU_activo boolean not null,
cuentaSuspendida boolean not null,
foreign key(cliente) references cliente(id),
foreign key(tipoCuenta) references tipoCuenta(id)
);

create table modoPago(
id int primary key,
descripcion varchar(30)
);

create table prestamo(
id int primary key,
cuenta bigint not null,
monto int not null,
fueAprobado boolean not null,
fueAcreditado boolean not null,
modoPago int,
fecha date not null,
foreign key(cuenta) references cuenta(numeroCuenta),
foreign key(modoPago) references modoPago(id)
);

create table cuentaTercero(
cuentaLocal bigint not null,
cuentaTercero bigint not null,
primary key(cuentaLocal,cuentaTercero),
foreign key(cuentaLocal) references cuenta(numeroCuenta),
foreign key(cuentaTercero) references cuenta(numeroCuenta)
);

create table planilla(
cuentaLocal bigint not null,
cuentaTercero bigint not null,
primary key(cuentaLocal,cuentaTercero),
foreign key(cuentaLocal) references cuenta(numeroCuenta),
foreign key(cuentaTercero) references cuenta(numeroCuenta)
);

create table proveedor(
cuentaLocal bigint not null,
cuentaTercero bigint not null,
primary key(cuentaLocal,cuentaTercero),
foreign key(cuentaLocal) references cuenta(numeroCuenta),
foreign key(cuentaTercero) references cuenta(numeroCuenta)
);

create table servicio(
id int primary key auto_increment,
descripcion varchar(30)
);

create table transaccion(
id int primary key auto_increment,
cuentaLocal bigint,
cuenatTercero bigint,
esDepositoTercero boolean,
esDepositoLocal boolean,
esPlanilla boolean,
esServicio boolean,
monto int not null,
fecha date
);

create table chequera(
noChequera int,
cuenta bigint,
primary key(noChequera,cuenta),
foreign key(cuenta) references cuenta(numeroCuenta)
);

create table chequeAutorizado(
noAutorizacion int primary key auto_increment,
noChequera int,
cuenta bigint,
noCheque int not null,
nombreCobrador varchar(50),
monto bigint,
foreign key(noChequera,cuenta) references chequera(noChequera,cuenta)
);

create table estadoCheque(
id int primary key auto_increment,
descripcion varchar(30) not null
);

create table cheque(
noCheque int not null,
noChequera int not null,
cuenta bigint not null,
estado int not null,
primary key(noCheque,noChequera,cuenta),
foreign key(noChequera,cuenta) references chequera(noChequera,cuenta),
foreign key(estado) references estadoCheque(id)
);

create table cobrador(
dpi bigint primary key,
primerNombre varchar(50),
segundoNombre varchar(50),
primerApellido varchar(50),
segundoApellido varchar(50)
);

create table chequeCobrado(
noTransaccion int primary key auto_increment,
noCheque int,
noChequera int,
cuenta bigint,
monto bigint not null,
cobrador bigint,
fecha date not null,
foreign key(cobrador) references cobrador(dpi),
foreign key(noCheque,noChequera,cuenta) references cheque(noCheque,noChequera,cuenta)
);

#select * from clienteIndividual;
#truncate table clienteIndividual;
#truncate table cliente;
#select * from cliente;


