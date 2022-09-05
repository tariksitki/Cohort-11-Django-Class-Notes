
from django.urls import path
from users.views import register, user_login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("register/", register, name="register"),
    path("user_login/", user_login, name="user_login"),
    path("logouts/", LogoutView.as_view(), name="logout_app")
]

