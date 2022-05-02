from django.db import models
from django.urls import reverse

class Bathroom(models.Model):
    """Bathroom Model"""

    # Fields
    location = models.CharField(max_length=1000, default='A Bathroom', help_text='Enter the bathroom location (e.g. Elmhurst Park Bathroom)')

    size = models.IntegerField(max_length=10, help_text='Enter how many stalls there are')

    cleanliness = models.IntegerField(max_length=10, default=5, help_text='Rate the cleanliness of the bathroom on a scale of 1 to 10')

    bathNum = models.IntegerField(max_length=1000, default=1000, help_text='Enter the bathroomID')

    class Meta:
        ordering = ['bathNum', 'location', '-size', '-cleanliness']

    def get_absolute_url(self):
        """Returns URL to specific instance of the Bathroom"""
        return reverse('Bathroom URL', args=[str9self.id0])

    def __str__(self):
         """String for representing the Bathroom name in the Admin site"""
         # Bathroom name will be the location of the bathroom
         return self.location

# Create your models here.
