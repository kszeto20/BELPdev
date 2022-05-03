from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('/listing', views.BathroomListView.as_view(), name='bathroom')

]
