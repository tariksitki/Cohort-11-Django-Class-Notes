

from importlib.resources import path


        ### token auth: 


from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, logout_view

urlpatterns = [
    path('login/', obtain_auth_token, name="login"),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view.as_view(), name='logout'),
]

#  obtain_auth_token  bu view bizden usernam eve password bekler ve bize token döner. 
