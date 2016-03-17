def price_comparison(request, itemname=None):
	form = ComparisonForm()
	if request.method == "POST":
		comparison_form = ComparisonForm(request.POST, itemname= itemname)
		if form.is_valid():
			dict_items = {}
			items = itemname
			for supermarket in retailer:
				costs = Costs.objects.values('unitcost', 'itemname','retailer','weight').annotate(frequency = Count('unitcost')).order_by('-frequency').filter(supermarket=retailer,itemname=itemname)
				results = []
				processed_items = [] 
				for cost in costs:
					if cost['itemname'] not in processed_items:
						processed_items.append(cost['itemname'])
						temp = {
							"frequency": cost['frequency'],
							"itemname": cost['itemname'],
							"unitcost": cost['unitcost'],
							"retailer": cost['retailer'],
							"weight": cost['weight'],
						}
						for item in costs:
							if item['itemname'] == temp['itemname']:
								if item['frequency'] > temp['frequency']:
									temp['frequency'] = item['frequency']
									temp['unitcost'] = item['unitcost']
									temp['retailer'] = item['retailer']
									temp['weight'] = item['weight']
						results.append(temp)

						dict_items["supermarket"] = unitcost

						return redirect('price_comparison', itemname=itemname)

			else:

				comparison_form = ComparisonForm()


			return render(request, 'food/price_comparison.html', {'costs':results })