from django.db import models
from django.contrib.admin import SimpleListFilter
from django.contrib import admin
# Create your models here.
from parroquia.models import parroquia

ESTADO_VISIBLE=[1,2]

class manejadorEstado(models.Manager):
	def get_query_set(self):
		default_queryset= super(manejadorEstado,self).get_query_set()
		return default_queryset.filter(status_in= ESTADO_VISIBLE)


#clase para crear farmacia en bd
class farmacia(models.Model):

	codfarmacia = models.AutoField(primary_key= True)
	rucFarmacia= models.CharField(max_length=13, null=False)
	nombrefarmacia = models.CharField(max_length= 30, null=False)
	nombrePropietario= models.CharField(max_length=50,null=False)
	apellidoPropietario= models.CharField(max_length=50, null=False)
	telffarmacia= models.CharField(max_length=10,null=False)
	direccion=models.CharField(max_length=50, null=False)
	latitud= models.FloatField(null=False)
	longitud= models.FloatField(null=False)
	email=models.EmailField(null=False)
	ESTADOS=((1,"PENDIENTE"),(2,"APROBADO"),(3,"DENEGADO"))
	estado=models.IntegerField(choices=ESTADOS, default=3)
	contrasenaFarm= models.CharField(max_length=13, null=False)
	erroresIngreso=models.CharField(max_length=100, null=False)
	codParroquia= models.ForeignKey(parroquia)


	def __str__(self):
			return '{} {}'.format(self.codfarmacia,self.rucFarmacia, self.nombrefarmacia, self.nombrePropietario, self.apellidoPropietario)
	

	def aprobar ( self , request , queryset ):
    		queryset.update ( estado = 2 )
  		aprobar.Short_Description="APROBAR FARMACIAS SELECCIONADAS"
		 
	def denegar ( self , request , queryset ):
    		queryset.update ( estado = 3)
    	denegar.short_description="DENEGAR FARMACIAS SELECCIONADAS"
	 	

class farmaciasAdmin(admin.ModelAdmin):
	list_filter=('estado','codParroquia__nombreParroquia',)
	ordering=('nombrefarmacia',)
	list_display=('codfarmacia', 'rucFarmacia', 'nombrefarmacia','nombrePropietario','apellidoPropietario','telffarmacia','email','estado')
   	search_fields=('rucFarmacia','nombrefarmacia','codParroquia__codParra','codParroquia__nombreParroquia')
   	Actions =('aprobar','denegar')
   

admin.site.register(farmacia,farmaciasAdmin)
