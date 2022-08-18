
from django.urls import path

from firstApp.views import home

urlpatterns = [
    path('', home),
]
