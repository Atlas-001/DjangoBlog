from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio),
    path("vista", vista),
    
]