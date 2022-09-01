from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'user_example/index.html')

def special(request):
    return render(request, "user_example/special.html")



def register(request):
    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
        ##  if yerine kullanilacak best practice
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    context = {
        "form" : form
    }

    return render(request, "user_example/registration/register.html", context)