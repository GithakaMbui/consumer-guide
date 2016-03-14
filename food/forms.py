from django import forms

from .models import Costs
from .models import UserProfile
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