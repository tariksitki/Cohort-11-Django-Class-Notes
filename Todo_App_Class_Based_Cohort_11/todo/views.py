from django.shortcuts import render
from todo.forms import TodoForm

from todo.models import Todo

# Create your views here.


    ####  CRUD OPERATIONS:

    ### read;  function based:

def home(request):
    todos = Todo.objects.all()
    form = TodoForm
    context = {
        "todos" : todos,
        "form" : form
    }
    
    return render(request, "todo/home.html", context)
