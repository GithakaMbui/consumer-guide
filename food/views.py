from django.shortcuts import render
from django.utils import timezone
from .models import Costs
from .models import Loans
from .models import Forex
from.models import Bureau
from .forms import CostForm
from .forms import UserForm, UserProfileForm
from .forms import ComparisonForm
from .forms import ForexComparisonForm
from .forms import LoanComparisonForm
from django.db.models import Count
from django.db.models import F
from django.views.generic.edit import FormView

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout

# Create your views here.


def item_list(request):
	#costs = Costs.objects.filter(dateprovided__lte=timezone.now()).order_by('dateprovided')
	#costs = Costs.objects.filter(itemname = "sugar")
	#costs = Costs.objects.all()
	#costs = Costs.objects.annotate(number_of_entries=Count('unitcost'))
	costs = Costs.objects.values('unitcost', 'itemname','retailer','weight').annotate(frequency = Count('unitcost')).order_by('-frequency')
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
	
	#print(results)	
	# highest_frequency = costs[0]
	#print(costs[0].number_of_entries)
	return render(request, 'food/item_list.html', {'costs':results })


def food_list(request):
	
	costs = Costs.objects.values('unitcost', 'itemname','retailer','weight').annotate(frequency = Count('unitcost')).order_by('-frequency')
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
	
	return render(request, 'food/food_list.html', {'costs':results })



def table_view(request):
	
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
	
	return render(request, 'food/table_view.html', {'costs':results })


def post_edit(request):
	#if request.method == "POST":
		form = CostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.dateprovided = timezone.now()
			post.save()
	
        	return render(request, 'food/post_edit.html', {'form': form})


def add_product(request):
	#if request.method == "POST":
		form = CostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.dateprovided = timezone.now()
			post.save()
	
        	return render(request, 'food/add_product.html', {'form': form})


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

def index(request):

	return render(request, 'food/index.html', {})


#user registration
def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'food/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )



#user login
def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/food/index')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'food/login.html', {})



# Use the login_required() decorator to ensure only those logged in can access the view.

def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/food/index/')


def forex(request):
	forexrate = Forex.objects.order_by('currency_name')[:5]
	context = {'forexrate': forexrate}
	return render(request, 'food/forex_rates.html', context)

def forex_rates(request):
	forexrate = Forex.objects.order_by('currency_name')[:5]
	context = {'forexrate': forexrate}
	return render(request, 'food/forex.html', context)

def forexby_bureau(request):
	instititution = Instititution.objects.order_by('inst_name')[:5]
	context = {'instititution': instititution}
	return render(request, 'food/forexby_bureau.html', context)



def loans(request):
	loanrate = Loans.objects.order_by('loan_name')[:5]
	context = {'loanrate': loanrate}
	return render(request, 'food/loan_rates.html', context)

# def compare(request):
# 	#item_comparison = Costs.objects.filter('outlet').annotate(higher_price= Count('unitcost'))
# 	item_comparison = Costs.objects.filter(itemname = 'sugar').annotate(higher_price__gt= F('unitcost'))
# 	context = {'item_comparison': item_comparison}
# 	return render(request, 'food/price_comparison.html', context)

# def price_comparison(request):
# 	form = ComparisonForm()
	# if request.method == "POST":
	# 	comparison_form = ComparisonForm(request.POST, itemname= itemname)
	# 	if comparison_form.is_valid():
	# 		dict_items = {}
	# 		items = itemname
	# 		for supermarket in retailer:
	# 			costs = Costs.objects.values('unitcost', 'itemname','retailer','weight').annotate(frequency = Count('unitcost')).order_by('-frequency').filter(supermarket=retailer,itemname=itemname)
	# 			results = []
	# 			processed_items = [] 
	# 			for cost in costs:
	# 				if cost['itemname'] not in processed_items:
	# 					processed_items.append(cost['itemname'])
	# 					temp = {
	# 						"frequency": cost['frequency'],
	# 						"itemname": cost['itemname'],
	# 						"unitcost": cost['unitcost'],
	# 						"retailer": cost['retailer'],
	# 						"weight": cost['weight'],
	# 					}
	# 					for item in costs:
	# 						if item['itemname'] == temp['itemname']:
	# 							if item['frequency'] > temp['frequency']:
	# 								temp['frequency'] = item['frequency']
	# 								temp['unitcost'] = item['unitcost']
	# 								temp['retailer'] = item['retailer']
	# 								temp['weight'] = item['weight']
	# 					results.append(temp)

	# 					dict_items["supermarket"] = unitcost

	# 					return redirect('price_comparison', itemname=itemname)

	# 	else:

			# comparison_form = ComparisonForm()


	# return render(request, 'food/price_comparison.html', {'form': form })




def price_comparison(request):
	"""
	Compare the price of different supermarkets
	on a particular item
	"""
	results = []

	if request.method == "POST":
		form = ComparisonForm(request.POST)
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
		form = ComparisonForm()

	return render(request, 'food/price_comparison.html', {'form': form,'results': results })



def forex_comparison(request):
	results=[]
	item = ''
	
	if request.method == "POST":
		form = ForexComparisonForm(request.POST)

		if form.is_valid():
			bureau = form.cleaned_data.get('bureau')
			item = form.cleaned_data.get('currency_name')


			for bureaus in bureau:
				b = Bureau.objects.get(inst_name=bureaus)
				forex = Forex.objects.filter(bureau=b,currency_name=item).values( 'currency_name','buying_price', 'selling_price' )
			

				temp = {
					'buying_price': 0,
					'selling_price':0,
				}

				for forexs in forex:

					temp['buying_price'] = forexs['buying_price']
					temp['frequency'] = forexs['selling_price']
					
					

				results.append({'buying_price': temp['buying_price'],'selling_price': temp['selling_price'] })



	else:
		form = ForexComparisonForm()

	return render(request, 'food/forex_comparison.html', {'form': form, 'item': item, 'results': results})



def loan_comparison(request):
	results=[]
	item = ''
	
	if request.method == "POST":
		form = LoanComparisonForm(request.POST)

		if form.is_valid():
			bank = form.cleaned_data.get('bank')
			item = form.cleaned_data.get('loan_name')


			for banks in bank:
				loan = Loans.objects.filter(bank=bank,loan_name=item).values( 'loan_name','loan_description', 'loan_amount' )
			

				temp = {
					'loan_name': loan_name,
					'loan_description': loan_description,
					'loan_amount': loan_amount,
				}

				results.append({'loan_name': temp['loan_name'],'loan_description': temp['loan_description'], 'loan_amount': loan_amount})



	else:
		form = LoanComparisonForm()

	return render(request, 'food/loan_comparison.html', {'form': form, 'item': item, 'results': results})
