from django.db import models
from django.utils import timezone

# Create your models here.


class Costs(models.Model):
	itemname = models.CharField(max_length=200)
	unitcost = models.IntegerField()
	weight = models.IntegerField(default = 1)
	dateprovided = models.DateTimeField(default = timezone.now)
	location = models.CharField(max_length=200)
	retailer = models.CharField(max_length=200, default='Nakumatt')
	

	def __unicode__(self):
		return self.itemname

class Outlet(models.Model):
	name = models.CharField(max_length=200)
	item = models.ManyToManyField(Costs)


	def __unicode__(self):
		return self.name

class Region(models.Model):
	name = models.CharField(max_length=200)
	outlet = models.ManyToManyField(Outlet)

	def __unicode__(self):
		return self.name