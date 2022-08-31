
from django.urls import path
from todo.forms import TodoForm
from todo.models import Todo

from todo.views import TodoCreate, TodoList, home, todo_add, todo_update
from django.views.generic import ListView


urlpatterns = [
    # path("", home, name="home"), ## read functional
    path("", TodoList.as_view(), name="homelist"), ## read class based in views.py

    # path("", ListView.as_view(model = Todo, context_object_name = "todos", ordering = ["priority"]), name="homelist"), ## read class based in urls.py

    # path("add/", todo_add, name="add"), ## create  functional view
    path("add/", TodoCreate.as_view(), name="add"), ## create  class based

    path("update/<int:id>/", todo_update, name="update"),

]