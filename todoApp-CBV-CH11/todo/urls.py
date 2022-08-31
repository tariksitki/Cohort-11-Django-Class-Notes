from django.urls import path

from todo.models import Todo
from .views import TodoCreate, TodoCreateList, TodoList, TodoUpdate, is_completed, todo_create, todo_update, todo_delete
from django.views.generic import ListView

urlpatterns = [
        ## read functional
    # path("", home, name="home"),

        ## 
    path("", TodoCreateList.as_view(), name="home"),

        ### read class based in views.py
    # path("list/", TodoList.as_view(), name="list"),

        ## views.py kullanmadan direkt burada. () icindeki parametre az ise böyle iyi
        #  best practice views de yapmak. 
    path("list/", ListView.as_view(model = Todo, context_object_name = "todos", ordering = ["priority"])),

        ## add functional
    # path("add/", todo_create, name="add"),
        
        ## add class based
    path("add/", TodoCreate.as_view(), name="add"),

        ## update functional
    # path("update/<int:id>", todo_update, name="update"),

        ## class based
    path("update/<int:pk>/", TodoUpdate.as_view(), name="update"),

        ## delete functional
    # path("delete/<int:id>", todo_delete, name="delete"),

        ### delete class based
    path("delete/<int:id>", todo_delete, name="delete"),

    path("done/<int:id>/", is_completed, name="done"),

]

