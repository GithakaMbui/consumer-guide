from django.db import models
from django.utils import timezone

# Create your models here.


class Costs(models.Model):
	itemname = models.CharField(max_length=200)
	unitcost = models.IntegerField()
	dateprovided = models.DateTimeField(default = timezone.now)
	location = models.CharField(max_length=200)
	

	def __unicode__(self):
		return self.itemname