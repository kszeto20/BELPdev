from django.shortcuts import render, redirect
from .models import Bathroom
from django.views import generic
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    """view function for home page of site"""

    num_bath = Bathroom.objects.all().count()

    context = {
        'num_bath' : num_bath,
        }
    return render(request, 'index.html', context = context)

def about(request):
    return render(request, "about.html")

def contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      subject = "Website Inquiry"
      body = {'first_name': form.cleaned_data['first_name'], 'last_name': form.cleaned_data['last_name'], 'email': form.cleaned_data['email_address'],'message':form.cleaned_data['message'],}
      message = "\n".join(body.values())
      message = "\n".join(body.values())
      try:
        send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
      except BadHeaderError:
        return HttpResponse('Invalid header found.')
      messages.success(request, "Message sent." )
      return redirect ("/listing")
    messages.error(request, "Error. Message not sent.")
  form = ContactForm()
  return render(request, "contacts.html", {'form':form})



# Create your views here.

class BathroomListView(generic.ListView):
    model = Bathroom
    context_object_name = 'bathroom_list'
    template_name = 'bathroom_list.html'

class BathroomDetailView(generic.DetailView):
    model = Bathroom
    template_name = 'bathroom_detail.html'
