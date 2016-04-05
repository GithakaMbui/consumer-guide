#views.py
#The cart comparison method to compare several food items at a go from different retailers/supermarkets
def cart_comparison(request):
	"""
	Compare the price of different supermarkets
	on a particular item
	"""
	results = []

	if request.method == "POST":
		form = CartComparisonForm(request.POST)
		print(form.is_valid())
		print (form.errors)
		print (request.POST)
		if form.is_valid():
			retailers = form.cleaned_data.get('retailer')
			item = form.cleaned_data.get('itemname')

			for retailer in retailers:

				total = 0

				for item in items:
			
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


					total = total + temp['unitcost']
					results.append({'total': total, 'retailer': retailer})

			
		

	else:
		form = CartComparisonForm()

	return render(request, 'food/cart_comparison.html', {'form': form,'results': results }) 


#forms.py
#I created a modelForm independ  from the other comparion from fromearlier


class CartComparisonForm(forms.ModelForm):
	retailer = forms.MultipleChoiceField( 
		widget=forms.CheckboxSelectMultiple, choices=OUTLETS_CHOICES)


	itemname = forms.ModelMultipleChoiceField(queryset = Costs.objects.all(),
		 widget  = forms.CheckboxSelectMultiple, )

	class Meta:
		model = Costs 
		fields = ('retailer',)
	

	def clean_retailer(self):

		data = self.cleaned_data['retailer']
		if len(data) < 2:
			raise forms.ValidationError("You must select at least two retailers")


		return data	


#UI
#The following is the front end code to display the retaile and the total for the items being comared.It is not working as of 26/03/2016

<form id="category_form" method="post" action="/food/cart_comparison/">
    {% csrf_token %}

      <label>Retailer</label>
      {{form.retailer}}
      <label>Item</label>
      {{form.itemname}}
    
      <input type="submit" name="submit" value="Compare Prices" />
  </form>

<br>

 
 {% if item %}
      Item: {{item}}
     <table class="table">
     <thead>
       <th>Retailer</th>
       <th>Cost</th>
     </thead>
      {% for result in results %}
      <tr>

      <td>{{ result.retailer }}</td>
      {% if result.unitcost == 0 %}
      <td>Item name has not been registered</td>
      {% else %}
      <td>{{result.unitcost}}</td>
      {% endif %}
      </tr>
      {% endfor %}

    

    </table>
{% endif %}    


#The errors printed on the terminal are as follows
False
<ul class="errorlist"><li>retailer<ul class="errorlist"><li>Select a valid choice. [u&#39;Nakumatt&#39;, u&#39;Tuskys&#39;] is not one of the available choices.</li></ul></li></ul>
<QueryDict: {u'itemname': [u'1', u'2'], u'csrfmiddlewaretoken': [u'SCcokCxHvF1EMHZBVSYJgFHqQlLMvjvv'], u'retailer': [u'Nakumatt', u'Tuskys'], u'submit': [u'Compare Prices']}>
[26/Mar/2016 11:19:15] "POST /food/cart_comparison/ HTTP/1.1" 200 11411
False
<ul class="errorlist"><li>retailer<ul class="errorlist"><li>Select a valid choice. [u&#39;Nakumatt&#39;, u&#39;Tuskys&#39;] is not one of the available choices.</li></ul></li></ul>
<QueryDict: {u'itemname': [u'1', u'2'], u'csrfmiddlewaretoken': [u'SCcokCxHvF1EMHZBVSYJgFHqQlLMvjvv'], u'retailer': [u'Nakumatt', u'Tuskys'], u'submit': [u'Compare Prices']}>
[26/Mar/2016 11:19:22] "POST /food/cart_comparison/ HTTP/1.1" 200 11411



