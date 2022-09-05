from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required

def home(request):
    # todos = Todo.objects.all()   user app den önce 
    todos = []
    if request.user.is_authenticated:  # euthenticate olmadi ise anonymis user
                                    ## sonuna () konulmaz.
        todos = Todo.objects.filter(user=request.user)

    form = TodoForm()
    
    context = {
        "todos" : todos,
        "form" : form
    }
    return render(request, "todo/home.html", context)




#### react daki private router gibi burada hazir decorator kullanilir. 


@login_required(login_url="user_login")  ## burada name pattern i yada static verilir
def todo_create(request):
    form = TodoForm()
    
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            # form.save()    user appp den önceki hali 
            todo = form.save(commit=False) # users app baglandiktan sonra
            todo.user = request.user
            todo.save()
            messages.success(request,"Todo created successfully")
            return redirect("home")
    
    context = {
        "form" : form
    }
    return render(request, "todo/todo_add.html", context)


@login_required(login_url="user_login")
def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(instance=todo)
    
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("home")
    
    context = {
        "todo" : todo,
        "form" : form
    }
    return render(request, "todo/todo_update.html", context)


@login_required(login_url="user_login")
def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    
    if request.method == "POST":
        todo.delete()
        messages.warning(request, "Todo deleted!")
        return redirect("home")
    
    context = {
        "todo": todo
    }
    return render(request, "todo/todo_delete.html", context)