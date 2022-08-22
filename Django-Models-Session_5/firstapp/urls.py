

from django.urls import path
from firstapp.views import firstapp

urlpatterns = [
    path("", firstapp)
]