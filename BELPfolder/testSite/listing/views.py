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

# Create your views here.

class BathroomListView(generic.ListView):
    model = Bathroom
