from django.forms import ModelForm, Textarea
from django.db import models

class Servicios(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.EmailField(max_length=100)
    email = models.CharField(max_length=100)
    
    class Meta:
        db_table = "servicios"


class Avaluos(models.Model):
    avaluoid = models.IntegerField(primary_key=True)
    coloniaid = models.IntegerField()
    clienteid = models.IntegerField()
    valuadorid = models.IntegerField()
    estatusid = models.IntegerField()
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()
    edad = models.IntegerField()
    dtsolicitud = models.DateField()
    dtvaluador = models.DateField()
    dtcliente = models.DateField()
    dtcobro = models.DateField()
    dtpago = models.DateField()
    manzana = models.CharField(max_length=50)
    lote = models.CharField(max_length=50)
    
    
    class Meta:
        managed = False
        db_table = "jos_av_avaluos"
        
        
        
class Clientes(models.Model):
    clienteid = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=250)
    
    
    class Meta:
        managed = False
        db_table = "jos_av_clientes"
        

class Tipos(models.Model):
    tipoid = models.IntegerField(primary_key=True)
    display = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=250)
    consecutivo= models.IntegerField()
    
    class Meta:
        managed = False
        db_table = "jos_av_tipos"
        
        
class Valuadores(models.Model):
    valuadorid = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=250)
    appaterno = models.CharField(max_length=250)
    apmaterno = models.CharField(max_length=250)
    display = models.CharField(max_length=10)
    
    class Meta:
        managed = False
        db_table = "jos_av_valuadores"
 
        
class Estatus(models.Model):
    estatusid = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    
    class Meta:
        managed = False
        db_table = "jos_av_estatus"
        
        
class Estados(models.Model):
    estadoid = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=250)
    clave = models.CharField(max_length=10)
    
    class Meta:
        managed = False
        db_table = "jos_estados"
        

class Municipios(models.Model):
    municipioid = models.IntegerField(primary_key=True)
    estadoid = models.IntegerField()
    nombre = models.CharField(max_length=250)
    
    class Meta:
        managed = False
        db_table = "jos_municipios"
        
        
class Colonias(models.Model):
    coloniaid = models.IntegerField(primary_key=True)
    municipioid = models.IntegerField()
    nombre = models.CharField(max_length=250)
    
    
    class Meta:
        managed = False
        db_table = "jos_colonias"