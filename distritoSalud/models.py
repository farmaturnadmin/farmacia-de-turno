from django.db import models

# Create your models here.
from django.contrib import admin
# Create your models here.

#clase para crear tabla distrito de salud en bd

class distritoSalud(models.Model):

	codDistrito = models.CharField(max_length=15, primary_key=True)
	nombreDistrito = models.CharField(max_length=50, null=False)
	def __str__(self):
			return '{} {}'.format(self.codDistrito, self.nombreDistrito)


class distritoAdmin(admin.ModelAdmin):
	
	list_display=('codDistrito','nombreDistrito')
    #list_filter=('nombrePropietario')
    #ordering=('nombrefarmacia',)
   	search_fields=('codDistrito','nombreDistrito')

admin.site.register(distritoSalud, distritoAdmin)