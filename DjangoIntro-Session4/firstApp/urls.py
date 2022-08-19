
from django.urls import path
from .views import drink_list, drink_detail

# from firstApp.views import home

# urlpatterns = [
#     path('', home),
# ]


urlpatterns = [
    path("", drink_list)
]