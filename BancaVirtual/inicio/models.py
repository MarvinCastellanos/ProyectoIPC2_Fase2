# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cheque(models.Model):
    nocheque = models.IntegerField(db_column='noCheque', primary_key=True)  # Field name made lowercase.
    nochequera = models.ForeignKey('Chequera', models.DO_NOTHING, db_column='noChequera')  # Field name made lowercase.
    cuenta = models.ForeignKey('Chequera', models.DO_NOTHING, db_column='cuenta')
    estado = models.ForeignKey('Estadocheque', models.DO_NOTHING, db_column='estado')

    class Meta:
        managed = False
        db_table = 'cheque'
        unique_together = (('nocheque', 'nochequera', 'cuenta'),)


class Chequeautorizado(models.Model):
    noautorizacion = models.AutoField(db_column='noAutorizacion', primary_key=True)  # Field name made lowercase.
    nochequera = models.ForeignKey('Chequera', models.DO_NOTHING, db_column='noChequera', blank=True, null=True)  # Field name made lowercase.
    cuenta = models.ForeignKey('Chequera', models.DO_NOTHING, db_column='cuenta', blank=True, null=True)
    nocheque = models.IntegerField(db_column='noCheque')  # Field name made lowercase.
    nombrecobrador = models.CharField(db_column='nombreCobrador', max_length=50, blank=True, null=True)  # Field name made lowercase.
    monto = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chequeautorizado'


class Chequecobrado(models.Model):
    notransaccion = models.AutoField(db_column='noTransaccion', primary_key=True)  # Field name made lowercase.
    nocheque = models.ForeignKey(Cheque, models.DO_NOTHING, db_column='noCheque', blank=True, null=True)  # Field name made lowercase.
    nochequera = models.ForeignKey(Cheque, models.DO_NOTHING, db_column='noChequera', blank=True, null=True)  # Field name made lowercase.
    cuenta = models.ForeignKey(Cheque, models.DO_NOTHING, db_column='cuenta', blank=True, null=True)
    monto = models.BigIntegerField()
    cobrador = models.ForeignKey('Cobrador', models.DO_NOTHING, db_column='cobrador', blank=True, null=True)
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'chequecobrado'


class Chequera(models.Model):
    nochequera = models.IntegerField(db_column='noChequera', primary_key=True)  # Field name made lowercase.
    cuenta = models.ForeignKey('Cuenta', models.DO_NOTHING, db_column='cuenta')

    class Meta:
        managed = False
        db_table = 'chequera'
        unique_together = (('nochequera', 'cuenta'),)


class Cliente(models.Model):
    clienteindividual = models.ForeignKey('Clienteindividual', models.DO_NOTHING, db_column='clienteIndividual', blank=True, null=True)  # Field name made lowercase.
    clienteempresarial = models.ForeignKey('Clienteempresarial', models.DO_NOTHING, db_column='clienteEmpresarial', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cliente'


class Clienteempresarial(models.Model):
    nit = models.IntegerField(primary_key=True)
    tipoempresa = models.ForeignKey('Tipoempresa', models.DO_NOTHING, db_column='tipoEmpresa')  # Field name made lowercase.
    nombreempresa = models.CharField(db_column='nombreEmpresa', max_length=30)  # Field name made lowercase.
    nombrecomercial = models.CharField(db_column='nombreComercial', max_length=30)  # Field name made lowercase.
    dpirepresentante = models.CharField(db_column='dpiRepresentante', max_length=20)  # Field name made lowercase.
    nombrerepersentante = models.CharField(db_column='nombreRepersentante', max_length=30)  # Field name made lowercase.
    apellidorepersentante = models.CharField(db_column='apellidoRepersentante', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clienteempresarial'


class Clienteindividual(models.Model):
    cui = models.IntegerField(primary_key=True)
    nit = models.IntegerField()
    primernombre = models.CharField(db_column='primerNombre', max_length=30)  # Field name made lowercase.
    segundonombre = models.CharField(db_column='segundoNombre', max_length=30)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='primerApellido', max_length=30)  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='segundoApellido', max_length=30)  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='fechaNacimiento')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clienteindividual'


class Cobrador(models.Model):
    dpi = models.BigIntegerField(primary_key=True)
    primernombre = models.CharField(db_column='primerNombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    segundonombre = models.CharField(db_column='segundoNombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='primerApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='segundoApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cobrador'


class Cuenta(models.Model):
    numerocuenta = models.AutoField(db_column='numeroCuenta', primary_key=True)  # Field name made lowercase.
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente')
    tipocuenta = models.ForeignKey('Tipocuenta', models.DO_NOTHING, db_column='tipoCuenta')  # Field name made lowercase.
    saldo = models.IntegerField()
    chequeau_activo = models.IntegerField(db_column='chequeAU_activo')  # Field name made lowercase.
    cuentasuspendida = models.IntegerField(db_column='cuentaSuspendida')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuenta'


class Cuentatercero(models.Model):
    cuentalocal = models.OneToOneField(Cuenta, models.DO_NOTHING, db_column='cuentaLocal', primary_key=True)  # Field name made lowercase.
    cuentatercero = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='cuentaTercero')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuentatercero'
        unique_together = (('cuentalocal', 'cuentatercero'),)


class Estadocheque(models.Model):
    descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'estadocheque'


class Modopago(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modopago'


class Planilla(models.Model):
    cuentalocal = models.OneToOneField(Cuenta, models.DO_NOTHING, db_column='cuentaLocal', primary_key=True)  # Field name made lowercase.
    cuentatercero = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='cuentaTercero')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'planilla'
        unique_together = (('cuentalocal', 'cuentatercero'),)


class Prestamo(models.Model):
    id = models.IntegerField(primary_key=True)
    cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='cuenta')
    monto = models.IntegerField()
    fueaprobado = models.IntegerField(db_column='fueAprobado')  # Field name made lowercase.
    fueacreditado = models.IntegerField(db_column='fueAcreditado')  # Field name made lowercase.
    modopago = models.ForeignKey(Modopago, models.DO_NOTHING, db_column='modoPago', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'prestamo'


class Proveedor(models.Model):
    cuentalocal = models.OneToOneField(Cuenta, models.DO_NOTHING, db_column='cuentaLocal', primary_key=True)  # Field name made lowercase.
    cuentatercero = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='cuentaTercero')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proveedor'
        unique_together = (('cuentalocal', 'cuentatercero'),)


class Servicio(models.Model):
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio'


class Tipocuenta(models.Model):
    descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipocuenta'


class Tipoempresa(models.Model):
    descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipoempresa'


class Transaccion(models.Model):
    cuentalocal = models.IntegerField(db_column='cuentaLocal', blank=True, null=True)  # Field name made lowercase.
    cuenattercero = models.IntegerField(db_column='cuenatTercero', blank=True, null=True)  # Field name made lowercase.
    esdepositotercero = models.IntegerField(db_column='esDepositoTercero', blank=True, null=True)  # Field name made lowercase.
    esdepositolocal = models.IntegerField(db_column='esDepositoLocal', blank=True, null=True)  # Field name made lowercase.
    esplanilla = models.IntegerField(db_column='esPlanilla', blank=True, null=True)  # Field name made lowercase.
    esservicio = models.IntegerField(db_column='esServicio', blank=True, null=True)  # Field name made lowercase.
    monto = models.IntegerField()
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaccion'
