
from django.db import models

from django.contrib import admin
# Create your models here.
from canton.models import canton



class parroquia(models.Model):

	codParro= models.CharField(max_length=10, primary_key= True)
	nombreParroquia= models.CharField(max_length=50, null =False)
	codcanton= models.ForeignKey(canton)
	def __str__(self):

			return '{} {}'.format(self.codParro, self.nombreParroquia)


class parroquiAdmin(admin.ModelAdmin):
	list_filter=('codcanton__nombreCanton',)
	list_display=('codParro','nombreParroquia')
    #list_filter=('nombrePropietario','nombrefarmacia')
    #ordering=('nombrefarmacia',)
   	search_fields=('codParro','nombreParroquia','codcanton__nombreCanton','codcanton__codigoCanton')

admin.site.register(parroquia,parroquiAdmin)