from django.db import models

from django.contrib import admin
# Create your models here.
from farmacia.models import farmacia
from turno.models import turno


#clase para crear tabla farmacia turno en bd
class farmaciaTurno(models.Model):

	codfarmacia= models.ForeignKey(farmacia)
	codTurno= models.ForeignKey(turno)

	
class farmaciaturnoAdmin(admin.ModelAdmin):
	list_filter=('codfarmacia__nombrefarmacia',)
	list_display=('codfarmacia','codTurno')
    #list_filter=('nombrePropietario','nombrefarmacia')
    #ordering=('nombrefarmacia',)
  	search_fields=('codfarmacia__rucFarmacia','codfarmacia__nombrefarmacia','codTurno__fechaInicio', 'codTurno__fechaFin')


admin.site.register(farmaciaTurno,farmaciaturnoAdmin)
