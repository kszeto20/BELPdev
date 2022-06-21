from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name="contact"),
    path('bathrooms/', views.BathroomListView.as_view(), name='bathrooms'),
    path('bathroom/<int:pk>', views.BathroomDetailView.as_view(), name='bathroom-detail'),
]
