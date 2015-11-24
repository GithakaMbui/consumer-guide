from django.shortcuts import render
from django.utils import timezone
from .models import Costs
from .forms import CostForm

# Create your views here.


def item_list(request):
	costs = Costs.objects.filter(dateprovided__lte=timezone.now()).order_by('dateprovided')
	return render(request, 'food/item_list.html', {'costs':costs})


def post_edit(request):
	#if request.method == "POST":
		form = CostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.dateprovided = timezone.now()
			post.save()
	
        	return render(request, 'food/post_edit.html', {'form': form})


		