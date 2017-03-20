from django.db import models

#from django.db import models

from django.contrib import admin
# Create your models here.



#clase para crear tabla turno en bd
class turno(models.Model):

	codturno = models.AutoField(primary_key= True)
	fechaInicio=models.DateField(null=False)
	fechafin=models.DateField(null=False)
	HoraInicio=models.TimeField(null=False)
	Horafin=models.TimeField(null=False)
	def __str__(self):
			return '{} {}'.format(self.fechaInicio, self.fechafin)

class turnoAdmin(admin.ModelAdmin):

	list_filter=('fechaInicio','fechafin',)
	list_display=('codturno','fechaInicio','fechafin','HoraInicio','Horafin')
    #list_filter=('nombrePropietario','nombrefarmacia')
    #ordering=('nombrefarmacia',)
   	search_fields=('fechafin','fechaInicio')

	
admin.site.register(turno,turnoAdmin)