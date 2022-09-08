from django.urls import include, path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import register, user_login, user_logout,home

urlpatterns = [
    path("", home, name="home"),
    path("login/",user_login,name="user_login"),
    path("register/",register,name="register"),
    path("logout/", user_logout, name="user_logout"),
]