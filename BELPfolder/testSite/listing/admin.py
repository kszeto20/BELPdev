from django.contrib import admin

from .models import Bathroom

@admin.register(Bathroom)
class BathroomAdmin(admin.ModelAdmin):
    list_display = ('bathNum', 'location', 'cleanliness', 'size')

    list_filter = ('size', 'cleanliness')

    fieldsets = (
        ('Information', { 'fields' : ('bathNum', 'location', 'gender')}),
        ('Ratings', { 'fields': ('size', 'cleanliness', 'comments', 'rating')}),

    )




# Register your models here.
