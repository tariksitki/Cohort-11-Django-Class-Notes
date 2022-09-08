from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import  login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserForm

def home(request):
    return render(request,'users/home.html')

def register(request):
    form_user = UserForm()
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        if form_user.is_valid():
            user = form_user.save()       
            login(request,user)
            messages.success(request,"You have been registered")
            
            return redirect('home')
    context = {
        'form_user': form_user,
    }

    return render(request, 'users/register.html', context)

def user_login(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if form.is_valid():
        user = form.get_user()#formdan gelen bilgileri alıyoruz
        login(request, user)#formda gelen bilgilerle istek atıyoruz
        messages.success(request,"You have been logged in")
        return redirect('home')

    return render(request, 'users/login.html', {'form': form})    
    #contexti burada da oluşturabilirz


def user_logout(request):
    messages.success(request,"You have been logged out")
    logout(request)
    return redirect('home')
    # return render(request, 'users/logout.html') 