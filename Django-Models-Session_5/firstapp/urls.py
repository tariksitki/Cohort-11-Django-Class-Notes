
from django.urls import path

from .views import firstapp


urlpatterns = [
    path("", firstapp)
]