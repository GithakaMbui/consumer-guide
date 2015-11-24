from django import forms

from.models import Costs

class CostForm(forms.ModelForm):

	class Meta:
		model = Costs
		fields = ('itemname', 'unitcost', 'retailer')