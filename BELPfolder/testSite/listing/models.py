from django.db import models
from django.urls import reverse

GENDER_CHOICES = (
    ('male','MALE'),
    ('female', 'FEMALE'),
    ('unisex', 'UNISEX')
)

RATING_NUMBERS = (
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
    (6,'6'),
    (7,'7'),
    (8,'8'),
    (9,'9'),
    (10,'10')
)



class Bathroom(models.Model):
    """Bathroom Model"""

    # Fields
    location = models.CharField(max_length=1000, default='A Bathroom', help_text='Enter the bathroom location (e.g. Elmhurst Park Bathroom)')

    size = models.IntegerField(max_length=2, choices=RATING_NUMBERS, default=3)

    cleanliness = models.IntegerField(max_length=2, default=5, choices=RATING_NUMBERS)

    bathNum = models.IntegerField(max_length=1000, default=1000, help_text='Enter the bathroomID')

    gender = models.CharField(max_length=6, choices =GENDER_CHOICES, default='Unisex')

    comments = models.CharField(max_length=250,default='No comments were made about this bathroom.', help_text= "Enter a brief description of your experience in the bathroom.  Please include any negatives or positives")
    
    rating = models.IntegerField(max_length=2, default=5, choices=RATING_NUMBERS)

    class Meta:
        ordering = ['bathNum', 'location', '-size', '-cleanliness', 'gender']

    def get_absolute_url(self):
        """Returns URL to specific instance of the Bathroom"""
        return reverse('bathroom-detail', args=[str(self.id)])

    def __str__(self):
         """String for representing the Bathroom name in the Admin site"""
         # Bathroom name will be the location of the bathroom
         return self.location

# Create your models here.
