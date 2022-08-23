

from django.urls import path

from secondapp.views import home_view

urlpatterns = [
    path("", home_view, name="home_view")
]

## name in unique olmasi gerekir.
