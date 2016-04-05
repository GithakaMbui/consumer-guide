from django import forms

from .models import (
	Costs,
	UserProfile,
	OUTLETS_CHOICES, FOOD_CHOICES
)

from .models import (
	Bureau,
	Forex,
	BUREAU_CHOICES
)
from .models import (
	Loans,
	BANK_CHOICES
)

from django.contrib.auth.models import User

class CostForm(forms.ModelForm):

	class Meta:
		model = Costs
		fields = ('itemname', 'unitcost', 'weight','retailer')


class UserForm(forms.ModelForm):
	 password = forms.CharField(widget=forms.PasswordInput())

	 class Meta:
	 	model = User
	 	fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website', 'picture')



class ComparisonForm(forms.ModelForm):
	retailer = forms.MultipleChoiceField( 
		widget=forms.CheckboxSelectMultiple, choices=OUTLETS_CHOICES)

	class Meta:
		model = Costs 
		fields = ('itemname',)
	

	def clean_retailer(self):

		data = self.cleaned_data['retailer']
		if len(data) < 2:
			raise forms.ValidationError("You must select at least two retailers")


		return data	



class CartComparisonForm(forms.ModelForm):
	retailer = forms.MultipleChoiceField( 
		widget=forms.CheckboxSelectMultiple, choices=OUTLETS_CHOICES)


	itemname = forms.MultipleChoiceField(choices = FOOD_CHOICES,
		 widget  = forms.CheckboxSelectMultiple, )

	class Meta:
		model = Costs 
		# fields = ('itemname',)
		exclude = ['unitcost', 'weight', 'dateprovided','location','itemname', 'retailer']
	

	# def clean_retailer(self):

	# 	data = self.cleaned_data['retailer']
	# 	if len(data) < 2:
	# 		raise forms.ValidationError("You must select at least two retailers")

	# 	return data	





class ForexComparisonForm(forms.ModelForm):
	bureau = forms.MultipleChoiceField(
		widget=forms.CheckboxSelectMultiple, choices=BUREAU_CHOICES)


	class Meta:
		model = Forex
		fields = ('currency_name',)


	def clean_bureau(self):

		data = self.cleaned_data['bureau']
		if len(data) < 2:
			raise forms.ValidationError("You must select atleast two forex bureaus")


		return data



class LoanComparisonForm(forms.ModelForm):
	bank = forms.MultipleChoiceField(
		widget=forms.CheckboxSelectMultiple, choices=BANK_CHOICES)


	class Meta:
		model = Loans
		fields = ('loan_name',)


	def clean_bureau(self):

		data = self.cleaned_data['banks']
		if len(data) < 2:
			raise forms.ValidationError("You must select atleast two banks")


		return data

		