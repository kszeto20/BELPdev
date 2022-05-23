from django.shortcuts import render
from .models import Bathroom
from django.views import generic

def index(request):
    """view function for home page of site"""

    num_bath = Bathroom.objects.all().count()

    context = {
        'num_bath' : num_bath,
        }
    return render(request, 'index.html', context = context)

# if you change index.html to bathroom_list.html the bathroom html will display instead of index. """
# When I make another function, I am not able to hav ethe program find the bathroom_list.html properly... it looks for it in listing/listingx
# Create your views here.

class BathroomListView(generic.ListView):
    model = Bathroom
