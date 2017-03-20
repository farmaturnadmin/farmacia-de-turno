from django.db import models


from django.contrib import admin
# Create your models here.
from provincia.models import provincia


#clase para crear tabla canto en bd
class canton(models.Model):

	codigoCanton = models.CharField(max_length=10, primary_key= True)
	nombreCanton= models.CharField(max_length=50, null=False)
	codProv= models.ForeignKey(provincia)

	def __str__(self):
			#return '{} {}'.format(self.codProv.provincia.codProvincia, self.codProv.provincia.nombreProvincia)
			return '{} {}'.format(self.codigoCanton, self.nombreCanton)


class cantonAdmin(admin.ModelAdmin):
	list_filter=('codProv__nombreProvincia',)
	list_display=('codigoCanton','nombreCanton')
    #list_filter=('nombrePropietario','nombrefarmacia')
    #ordering=('nombrefarmacia',)
   	search_fields=('codigoCanton','nombreCanton', 'codProv__nombreProvincia','codProv__codProvincia')

admin.site.register(canton,cantonAdmin)