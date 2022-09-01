from django.urls import path, include
from .views import (
    home,
    special,
    register
)

### import esnasinda view lari alt alta yazarsak yoruma alma da kolay olur

urlpatterns = [
    path('', home, name="home"),
    path('special/', special, name="special"),
    path('register/', register, name="register"),
]
