from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm
from django.contrib import messages


    ### class based views imports

from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy


    ### functional read
# def home(request):
#     todos = Todo.objects.all()
#     form = TodoForm()
    
#     context = {
#         "todos" : todos,
#         "form" : form
#     }
#     return render(request, "todo/home.html", context)



    ### class based read
class TodoList(ListView):
    model = Todo
    # default context_object_name  modeladi_list yani todo_list   eger bu sekilde yaziyorsak tekrar belirtmeye gerek yok. ama biz degistiriyoruz o nedenle gerek var
    context_object_name = "todos"
    ## default  template_name   todo/todo_list.html
    ordering = ["priority"]  ## bu islemi func da view da todos = Todo.objects.all().order_by()  seklinde yapariz. 
    # db de tablomuzda default siralama id ye göre. biz burada tablonun orijinalini degistirmiyoruz. user in gördügü kismi degistiriyoruz. iki verinin priority si esit ise bu durumda id ye bakar. 
    # tersten siralanmasi icin ordering = ["-priority"] basina eksi



### eger istersek bu kodlari hiv views.py da yazmayiz direkt urls.py da yazariz.






    ## functional create

def todo_create(request):
    form = TodoForm()
    
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Todo created successfully")
            return redirect("home")
    
    context = {
        "form" : form
    }
    return render(request, "todo/todo_add.html", context)




    ### class based create

class TodoCreate(CreateView):
    model = Todo 
    form_class = TodoForm  ## burada sonuna () konulmaz
    template_name = "todo/todo_add.html" # default todo/todo_form.html
    success_url = reverse_lazy("")  # o isin yapildigini göster isi agirdan al


class TodoCreateList(CreateView):
    model = Todo
    form_class = TodoForm  # burada sonuna () konulmaz
    template_name = "todo/home.html"  # default todo/todo_form.html
    success_url = reverse_lazy("")  # o isin yapildigini göster isi agirdan al

    def get_context_data(self, **kwargs):
        kwargs["todos"] = Todo.objects.order_by("-priority")
        kwargs["done_count"] = Todo.objects.filter(is_done = True).count()
        return super(TodoCreateList, self).get_context_data(**kwargs)



## funcional larda view func icinde bir degisken tanimlayip bunu context icinde koyup gönderiyoruz. ama class da bir veri göndermek icin get_context_data methodu overview edilmeli






    ### functional update:

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



    # class based update:


class TodoUpdate(UpdateView):
    model = Todo 
    form_class = TodoForm
    template_name = "todo/todo_update.html"  #  default todo/todo_update_form.html
    # pk_url_kwarg = "id" ## default pk  eger id yerine pk kullanirsak yazmayiz
    success_url = reverse_lazy("home")








    ## functional delete:

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





        ### class based delete:










def is_completed(request, id):
    todo = Todo.objects.get(id=id)
    todo.is_done = not(todo.is_done)
    todo.save()
    return redirect("home")
