from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bathrooms', views.BathroomListView.as_view(), name='bathroom')
]
