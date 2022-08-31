from django.shortcuts import render, redirect
from todo.forms import TodoForm

from todo.models import Todo
from django.contrib import messages

# Create your views here.

    ## class based imports:
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

### Önemli:  class based view leri views.py da yazmak orunda degiliz. eger class icine yazacagimiz parametreler az ise direkt olarak urls.py da da yazilabilir. bunun icin read  de bir örnek yaptik. 


## Önemli:  class based views lerde message kullanma adimlari:
        ### views.py
## 1: from django.contrib import messages
## 2: from django.contrib.messages.views import SuccessMessageMixin.
##   class ismi yanina acilan ve nereden inherit edileceginin yazildigi parantez icine ilk props olarak SuccessMessageMixin  yazilir. 
## 3: yazdigimiz class icinde ve en üste """ """ icinde mesaj yada
## 4: yazdigimiz class icine property olarak  success_message = "%(book)s was updated successfully"
## 5: son olarak da bu class based view in bize return edecegi template e yada base.html e messages ile ilgili olan for döngüsü yazilir


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




    ### read;  class based:

class TodoList(ListView):
    model = Todo
    context_object_name = "todos"
    # ordering= ['priority'] #sıralama işlemi asc
    ordering= ['-priority'] #sıralama işlemi desc
    def get_context_data(self, **kwargs):
        kwargs["form"] = TodoForm
        kwargs["todos"] = Todo.objects.order_by("-priority")
        kwargs["done_count"] = Todo.objects.filter(is_done=True).count()
        return super(TodoList, self).get_context_data(**kwargs)

    ## Önemli:  ListView da form_class diye bir attribute yoktur. sadece CreateView da vardir. Bu nedenle template imize form göndermek icin context yolunu tercih ettik. class based lerde de context gönderimi get_context_data methodunun overwrite edilmesi ile olur.

    ## Buradaki context_object_name = "todos"  bizim funcional view daki context e karsilik gelir. orada biz todos = Todo.objects.all diyorduk ve todos u context icine atiyorduk. Burada ise Todo modeline ait tüm verileri kendisi otomatik olarak context icinde gönderir. biz burada sadece isminde ayarlama yapariz.
    # default context_object_name  modeladi_list yani todo_list   eger bu sekilde yaziyorsak tekrar belirtmeye gerek yok. ama biz degistiriyoruz o nedenle gerek var
    ## default  template_name   todo/todo_list.html. bizim ki bu sekilde oldugu icin burada tekrar yazma ihtiyaci olmadi
    # db de tablomuzda default siralama id ye göre. biz burada tablonun orijinalini degistirmiyoruz. user in gördügü kismi degistiriyoruz. iki verinin priority si esit ise bu durumda id ye bakar. 
    # tersten siralanmasi icin ordering = ["-priority"] basina eksi






    ### create;   functional views:

def todo_add(request):
    form = TodoForm
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo created succesfully")
            return redirect("homelist")
    context = {
        "form" : form 
    }
    return render(request, "todo/todo_add.html", context)



    ### create;   class based: 
    ## Öncelikle yalin halde yazacagiz daha sonra context li olani yazacagiz.

# class TodoCreate(SuccessMessageMixin,CreateView):
#     """  Hello """
#     model = Todo 
#     form_class = TodoForm  # burada sonuna () konulmaz
#     template_name = "todo/todo_add.html"  ## defaultu; "todo/todo_form.html"
#     success_url = reverse_lazy("list") ## isin yapildigini göster isi agirdan al
#     success_message = "Todo created succesfully"




    ### class based create with context:

class TodoCreate(SuccessMessageMixin,CreateView):
    """  Hello """
    model = Todo 
    form_class = TodoForm  # burada sonuna () konulmaz
    ## form_class ListView de yoktur. bu nedenle read de kullanmadik
    template_name = "todo/todo_add.html"  ## defaultu; "todo/todo_form.html"
    success_url = reverse_lazy("homelist") ## #reverse_lazy functionlardaki redirectin yerine kullanılıyor
    success_message = "Todo created succesfully"

    def get_context_data(self, **kwargs):
        kwargs["todos"] = Todo.objects.order_by("-priority")
        kwargs["done_count"] = Todo.objects.filter(is_done=True).count()
        return super(TodoCreate, self).get_context_data(**kwargs)

## Note: Buradaki get_context_data  methodunu neden yazdik?  Functional view larda, context gönderimi cok basit bir sekilde gerceklesiyordu. Burada ise kendi istedigimiz ekilde bir context göndermek icin get_context_data methodunu overview etmemiz gerekir. kwargs["todos"]  seklinde bir yazim sebebi:  göndermek istedigimiz context, class in orijinalinde dict formatinda yazilmistir. iste bu sekilde yazarak dict e bir eleman ekliyoruz.  Bu verileri template e göndererek ne yapacagiz? toplam todo sayisi / is_done seklinde user a göstermek istiyoruz. template de yakalarken; todos ve done_count seklinde yakalayacagiz. 


    






    #### functional update:

def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(instance=todo)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            redirect("homelist")
    context = {
        "form" : form,
        "todo" : todo
    }
    return render(request, "todo/todo_update.html", context)
    

