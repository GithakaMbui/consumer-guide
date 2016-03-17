from django import forms

from .models import (
	Costs,
	UserProfile,
	OUTLETS_CHOICES
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


		