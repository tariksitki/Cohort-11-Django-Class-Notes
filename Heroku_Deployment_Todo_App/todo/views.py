from django.shortcuts import render, redirect
from django.http import HttpResponse

from todo.forms import TodoForm
from .models import Todo

from django.contrib import messages


# Create your views here.

    ## read :

def home(request):
    # return render(request, "")
    todos = Todo.objects.all()

    ## hem form ekleme hem de bilgileri ayni sayfada görmek icin:
    form = TodoForm() 

    context = {
        "todos" : todos, 
        "form" : form
    }

    return render(request, "todo/home.html", context)



###  create todos:


def todo_create(request):
    form = TodoForm()
    context = {
        "form" : form
    }
    if request.method == "POST":
        form = TodoForm(request.POST) # post objesi icinde gelen veriler form icine koy
        if form.is_valid:
            form.save()
            messages.success(request,"Todo created successfully")
            return redirect("home")
    ## burada modelform kullanmasaydik islemlerimiz uzun olacakti. 

    return render(request, "todo/todo_add.html",context)



## add islemini home a alma icin, yani hem ekleme hem de read islemini ayni template de yapmak icin, ya add in view inde bulunan form validation islemlerini home a kopyalayacagiz yada template de formun action isleminde "add/" yazacagiz. istek yaptigimizda views daki add func i calistirir 






### update :

def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(instance=todo)
    context = {
        "todo" : todo,
        "form" : form
    }

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo) ## create den tek farki 
        if form.is_valid:
            form.save()
            return redirect("home")

    return render(request, "todo/todo_update.html", context)








#### delete:

def delete_todo(request, id):
    todo = Todo.objects.get(id=id)

    context = {
        "todo" : todo
    }

    if request.method == "POST":
        todo.delete()
        messages.warning(request, "Todo deleted!")
        return redirect("home")

    return render(request, "todo/todo_delete.html", context)