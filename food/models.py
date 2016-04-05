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
	('Sugar','Sugar'),
	('Kimbo Cooking Fat', 'Kimbo Cooking Fat'),
	('Broadways Whole Loaf','Broadways Whole Loaf'),
	('Salt', 'Salt'),
	)

WEIGHT_CHOICES = (
	('1', '1 KG'),
	('2', '2 KG'),
	('500', '500 mg'),
	)

BUREAU_CHOICES = (

	('DTBBureau', 'DTBBureau'),
	('SkyBureau', 'SkyBureau'),
	('Nationalbureau', 'Nationalbureau'),
	('IMBureau', 'IMBureau'),
	('FinaBureau', 'FinaBureau'),

	)

CURRENCY_CHOICES = (

	('USD', 'USD'),
	('EURO', 'EURO'),
	('TZSH', 'TZSH'),
	('UGSH', 'UGSH'),
	('BPD', 'BPD'),
	('BPD', 'BPD')

	)


BANK_CHOICES = (

	('Barclays', 'Barclays'),
	('KCB', 'KCB'),
	('Stanchart', 'Stanchart'),
	('Co-op', 'Co-op'),
	('Uwezo', 'Uwezo'),
	('Uwezo', 'Uwezo')

	)


LOAN_CHOICES = (

	('House Mortgage', 'House Mortgage'),
	('Biashara', 'Biashar'),
	('Personal', 'Personal'),
	('Chama', 'Chama'),
	('Car', 'Car'),
	('Commercial', 'Commercial')

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
	loan_name = models.CharField(max_length=250, choices=LOAN_CHOICES)
	loan_description = models.CharField(max_length=400)
	requirements = models.CharField(max_length=300)
	loan_amount = models.IntegerField(default = 50000)
	bank = models.CharField(max_length=300 ,  default = "Barclays", blank=True, null=True, choices=BANK_CHOICES)
	#bank = models.ForeignKey(Banks)


	def __unicode__(self):
		return self.loan_name


class Bureau(models.Model):
	#inst_id = models.IntegerField()
	inst_name = models.CharField(max_length=300, default = "SkyBureau", blank=True, null=True, choices=BUREAU_CHOICES)
	webpage = models.CharField(max_length=300)
	#type_name = models.ForeignKey(Institution_type, on_delete=models.CASCADE)
	bureau_type = models.CharField(max_length=300)

	def __unicode__(self):
		return self.inst_name


class Forex(models.Model):
	currency_name = models.CharField(max_length=300, choices=CURRENCY_CHOICES)
	buying_price = models.IntegerField()
	selling_price = models.IntegerField()
	#inst_id = models.ForeignKey(Instititution, on_delete=models.CASCADE)
	bureau = models.ForeignKey(Bureau, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.currency_name






#class Institution_type(models.Model):
	#type_id = models.IntegerField()
	#inst_id = models.ForeignKey(Instititution, on_delete=models.CASCADE)
	#type_name = models.CharField(max_length=300)



