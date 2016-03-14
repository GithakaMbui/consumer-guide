from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

OUTLETS_CHOICES = (
	('Nakumatt', 'Nakumatt'),
	('Tuskys', 'Tuskys'),
	('Naivas', 'Naivas'),
	('Ukwala', 'Ukwala'),
	('Uchumi', 'Uchumi'),
	)

FOOD_CHOICES = (
	('Jogoo Maize Flour', 'Jogoo Maize Flour'),
	('EX Wheat flour', 'EX Wheat flour'),
	('Mumias Sugar','Mumias Sugar'),
	('Kimbo Cooking Fat', 'Kimbo Cooking Fat'),
	('Broadways Whole Loaf','Broadways Whole Loaf'),
	)

WEIGHT_CHOICES = (
	('1', '1 KG'),
	('2', '2 KG'),
	('500', '500 mg'),
	)



class Costs(models.Model):
	itemname = models.CharField(max_length=200, choices=FOOD_CHOICES)
	unitcost = models.IntegerField()
	weight = models.IntegerField(default = 1, choices=WEIGHT_CHOICES)
	dateprovided = models.DateTimeField(default = timezone.now)
	location = models.CharField(max_length=200)
	retailer = models.CharField(max_length=200, choices=OUTLETS_CHOICES)
	

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

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	def __unicode__(self):
		return self.user.username



class Banks(models.Model):
	bank_name = models.CharField(max_length=300)
	bank_type = models.CharField(max_length=300)
	webpage = models.CharField(max_length=300)

	def __unicode__(self):
		return self.bank_name


class Loans(models.Model):
	loan_name = models.CharField(max_length=250)
	loan_description = models.CharField(max_length=400)
	requirements = models.CharField(max_length=300)
	bank = models.ForeignKey(Banks, on_delete=models.CASCADE)


	def __unicode__(self):
		return self.loan_name


class Instititution(models.Model):
	#inst_id = models.IntegerField()
	inst_name = models.CharField(max_length=300, default = "SKY", blank=True, null=True)
	webpage = models.CharField(max_length=300)
	#type_name = models.ForeignKey(Institution_type, on_delete=models.CASCADE)
	Institution_type = models.CharField(max_length=300)

	def __unicode__(self):
		return self.inst_name


class Forex(models.Model):
	currency_name = models.CharField(max_length=300)
	buying_price = models.IntegerField()
	selling_price = models.IntegerField()
	#inst_id = models.ForeignKey(Instititution, on_delete=models.CASCADE)
	Instititution = models.ForeignKey(Instititution, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.currency_name






#class Institution_type(models.Model):
	#type_id = models.IntegerField()
	#inst_id = models.ForeignKey(Instititution, on_delete=models.CASCADE)
	#type_name = models.CharField(max_length=300)



