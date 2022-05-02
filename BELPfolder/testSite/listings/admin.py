from django.contrib import admin

from .models import Bathroom

@admin.register(Bathroom)
class BathroomAdmin(admin.ModelAdmin):
    list_display = ('bathNum', 'location', 'cleanliness', 'size')

    list_filter = ('size', 'cleanliness')

    fieldsets = (
        (None, { 'fields' : ('bathNum', 'location')}),
        ('Ratings', { 'fields': ('size', 'cleanliness')}),

    )




# Register your models here.
