from django.contrib import admin
from .models import Costs
from .models import UserProfile
# Register your models here.

class CostAdmin(admin.ModelAdmin):
	list_display = ('itemname', 'unitcost', 'retailer')
	search_fields = ('itemname',)
	list_filter = ('itemname',)
	


	


admin.site.register(Costs, CostAdmin)
admin.site.register(UserProfile)

