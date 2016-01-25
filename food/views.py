from django.shortcuts import render
from django.utils import timezone
from .models import Costs
from .forms import CostForm
from django.db.models import Count

# Create your views here.


def item_list(request):
	#costs = Costs.objects.filter(dateprovided__lte=timezone.now()).order_by('dateprovided')
	#costs = Costs.objects.filter(itemname = "sugar")
	#costs = Costs.objects.all()
	#costs = Costs.objects.annotate(number_of_entries=Count('unitcost'))
	costs = Costs.objects.values('unitcost', 'itemname').annotate(frequency = Count('unitcost')).order_by('-frequency')
	results = []
	processed_items = [] 

	for cost in costs:
		if cost['itemname'] not in processed_items:
			processed_items.append(cost['itemname'])
			temp = {
				"frequency": cost['frequency'],
				"itemname": cost['itemname'],
				"unitcost": cost['unitcost']
			}
			for item in costs:
				if item['itemname'] == temp['itemname']:
					if item['frequency'] > temp['frequency']:
						temp['frequency'] = item['frequency']
						temp['unitcost'] = item['unitcost']
			results.append(temp)
	
	#print(results)	
	# highest_frequency = costs[0]
	#print(costs[0].number_of_entries)
	return render(request, 'food/item_list.html', {'costs':results })


def post_edit(request):
	#if request.method == "POST":
		form = CostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.dateprovided = timezone.now()
			post.save()
	
        	return render(request, 'food/post_edit.html', {'form': form})


def home(request):
	#costs = Costs.objects.filter(dateprovided__lte=timezone.now()).order_by('dateprovided')
	#costs = Costs.objects.filter(itemname = "sugar")
	#costs = Costs.objects.all()
	#costs = Costs.objects.annotate(number_of_entries=Count('unitcost'))
	costs = Costs.objects.values('unitcost', 'itemname').annotate(frequency = Count('unitcost')).order_by('-frequency')
	results = []
	processed_items = [] 

	for cost in costs:
		if cost['itemname'] not in processed_items:
			processed_items.append(cost['itemname'])
			temp = {
				"frequency": cost['frequency'],
				"itemname": cost['itemname'],
				"unitcost": cost['unitcost']
			}
			for item in costs:
				if item['itemname'] == temp['itemname']:
					if item['frequency'] > temp['frequency']:
						temp['frequency'] = item['frequency']
						temp['unitcost'] = item['unitcost']
			results.append(temp)
	
	#print(results)	
	# highest_frequency = costs[0]
	#print(costs[0].number_of_entries)
	return render(request, 'food/home.html', {'costs':results })

