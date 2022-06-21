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

def contact(request):
	return render(request, 'contacts.html')

# Create your views here.

class BathroomListView(generic.ListView):
    model = Bathroom
    context_object_name = 'bathroom_list'
    template_name = 'bathroom_list.html'

class BathroomDetailView(generic.DetailView):
    model = Bathroom
    template_name = 'bathroom_detail.html'
