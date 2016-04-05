def price_comparison(request):
	"""
	Compare the price of different supermarkets
	on a particular item
	"""

	results = []
	item = ''
	if request.method == "POST":
		form = ComparisonForm(request.POST)

		if form.is_valid():
			retailers = form.cleaned_data.get('retailer')
			item = form.cleaned_data.get('itemname')
			
			for retailer in retailers:
				costs = Costs.objects.filter(
					retailer=retailer, 
					itemname__icontains=item).values('unitcost', 'itemname').annotate(
						frequency = Count('unitcost')).order_by('-frequency')
				
				temp = {
					'unitcost': 0,
					'frequency':0,
				}

				for cost in costs:
					if cost['frequency'] > temp['frequency']:
						temp['unitcost'] = cost['unitcost']
						temp['frequency'] = cost['frequency']

				results.append({'unitcost': temp['unitcost'], 'retailer': retailer})

			#print results	



	else:
		form = ComparisonForm()



	return render(request, 'food/price_comparison.html', {'form': form, 'item': item, 'results': results })