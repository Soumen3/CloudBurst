from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('historical_data/',views.historicalData, name='historicalData'),
    path('contact/', views.contact, name='contact'),
    path('alert/', views.alert, name='alert'),
    path('about/', views.about, name="about"),
]
