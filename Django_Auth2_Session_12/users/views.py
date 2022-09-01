from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages

from users.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    return render(request, 'users/home.html')


        #### logout

## navbar daki logout tusunu aktif ediyoruz ve tiklandiginda logout a yönlendiriyor.
## önce logut func view de yazilir. 
## sonra bu view i tetikleyecek url yazilir. 
## eger bu url i elimizle yazmak istemezsek, o zaman bu url i calistiracak bir tus yapilir. a  tagina href vererek bu islem yaptirilir.
def user_logout(request):
    logout(request)
    return redirect("home")


## Bu islemlere mesaj ekleyelim. 




        ### register:
## bunun icin form kullanmak gerekir. ama biz iki model kullaniyoruz. django nun user modeli ve bizim kendi modelilmiz. ikisi icinde ayri form gerekir. 


def register(request):
    form_user = UserForm()
    form_profile = UserProfileForm()
    if request.method == "POST":
        form_user = UserForm(request.POST)
        form_profile = UserProfileForm(request.POST, request.FILES)
        ## burada foto oldugu icin files. dosyalar bu sekilde kaydedilir. 
        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save()
            profile = form_profile.save(commit=False) # burada formdan gelen bilgiler bir profil olusturur ama kaydedilmez bekler. 
            profile.user = user
            profile.save()
            login(request, user)  ## kaydolan user login yapilir. 
            ## 3. tablomuz olsaydi user yine yapilacakti digerleri bekleyecekti. 
            ## commit, sql den gelir. rollback hepsini iptal eder. 
             
            return redirect("home")
            ## burada 1. tablodan id yi almamiz lazim. o nedenle user tablosunu önce kaydetmemiz yeterli degil. 

    context = {
        "form_user" : form_user,
        "form_profile" : form_profile
    }
    return render(request, "users/register.html", context)






    #### login:


def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user=form.get_user()
        login(request, user)
        return redirect("home")

    return render(request, "users/login.html", {"form" : form})