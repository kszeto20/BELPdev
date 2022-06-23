from this import d
from django import forms
from .models import Bathroom
# Create your forms here.

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    email_address = forms.EmailField(max_length = 150)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)


 
# create a ModelForm
class BathroomForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Bathroom
        fields = ("__all__")
        

    
