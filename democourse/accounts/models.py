from django.db import models

# Create your models here.

class Custumer(models.Model):
	"""
	Description: Model Description
	"""
	name = models.CharField(max_length=200)
	price = models.FloatField()
	email =  models.CharField(max_length=200)
	data_created = models.DateTimeField(auto_now_add=True, null=True)   

	class Meta:
		ordering = ('price',)
	pass