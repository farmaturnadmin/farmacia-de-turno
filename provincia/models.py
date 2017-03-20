from django.db import models

from django.contrib import admin
# Create your models here.
from distritoSalud.models import distritoSalud


#clase para crear tabla provincia en bd
class provincia(models.Model):

	codProvincia = models.CharField(max_length=10, primary_key= True)
	nombreProvincia= models.CharField(max_length=50, null=False)
	coddistritoSalud= models.ForeignKey(distritoSalud)
	def __str__(self):
			return '{} {}'.format(self.codProvincia, self.nombreProvincia)
	
			return '{} {}'.format(self.coddistritoSalud.distritoSalud.codDistrito, self.coddistritoSalud.distritoSalud.nombreDistrito)


class provinciaAdmin(admin.ModelAdmin):
	list_filter=('coddistritoSalud__codDistrito','coddistritoSalud__nombreDistrito',)
	list_display=('codProvincia','nombreProvincia')
    #list_filter=('coddistritoSalud')
    #ordering=('nombrefarmacia',)
   	search_fields=('codProvincia','nombrePovincia','coddistritoSalud__codDistrito','coddistritoSalud__nombreDistrito')
admin.site.register(provincia, provinciaAdmin)