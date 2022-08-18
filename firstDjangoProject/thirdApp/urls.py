

from django.urls import path

from thirdApp.views import home

urlpatterns = [
    path('', home),
]
