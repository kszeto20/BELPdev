from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contact, name='contacts'),
    path('about/', views.about, name='about'),
    path('bathrooms/', views.BathroomListView.as_view(), name='bathrooms'),
    path('bathroom/<int:pk>', views.BathroomDetailView.as_view(), name='bathroom-detail'),
    path('add_bathroom/', views.add_bathroom, name='add_bathroom'),
]
