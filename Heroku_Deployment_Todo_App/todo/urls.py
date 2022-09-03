
from django.urls import path

from todo.views import home, todo_create, todo_update, delete_todo


urlpatterns = [
    path("", home, name="home"),
    path("add/", todo_create, name="add"),
    path("update/<int:id>/", todo_update, name="update"),
    path("delete/<int:id>/", delete_todo, name="delete"),

]