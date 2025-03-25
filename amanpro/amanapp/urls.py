from .views import *
from django.urls import path


urlpatterns = [
    path('registerdetails/', NewRequestView.as_view(), name='register'),
    
    ]