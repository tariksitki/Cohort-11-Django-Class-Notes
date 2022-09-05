
from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

from users.forms import UserForm, UserProfileForm


## Önemli:  UserCreationForm  eger bu formu cagirirsak sadece username ve password ile giris yaptirir default oalarak.ama biz email de isteriz. Bu nedenle bu formu forms.py da overwrite ettik. 

        ## ilk önce bunu yaptik sonra iki farkli form yapip asagidaki kodu yazdik 
# def register(request):
#     # request.POST or None
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()  ## buradan sonraki islemler register olan login olsun diye
#             username = form.cleaned_data["username"]     ## formu print edelim. input lar halinde gelir. biz bu inputlar icindeki veriyi alacagiz. valid olmus formdan bize username isimli inputu getir. 
#             password = form.cleaned_data["password1"]  ## dict formatinda geldiginden [] kullanarak veri aliyoruz. buradaki password1 i inspect yapip html kismindan aldik.
#             user = authenticate(username = username, password = password) ## user i auth yaptiktan sonra bilgilerini user degiskenine ata. ve bu bilgiler ile login yap. 
#             login(request, user)
#             return redirect("home")
#     else:  ## get istegi
#         form = UserCreationForm() # user get yaptiginda icini bos birakarak gönder

#     return render(request, "registration/register.html", {"form" : form})

        


    ### POST kismindan text bilgilerini aliriz. dosyalari da files dan

def register(request):
    form_user = UserForm()
    form_profile = UserProfileForm()
    if request.method == "POST":
        form_user = UserForm(request.POST)
        form_profile = UserProfileForm(request.POST, request.FILES)

        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save()
            # profile = form_profile().save()
            ## bu sekilde yaparsak hicbir degisiklik olmadna kaydetmis oluurz. ama biz bazi degisiklikler yapmak isteriz. o nednele bekle deriz. 
            profile = form_profile.save(commit=False)  ## burada amacimiz db ye kaydetmek degil. böyle diyerek db ye kaydetmesini engelliyoruz. Veriyi dict formatinda almaya calisiyoruz. cleaned data ile veriyi almaya benziyor. 
            profile.user = user ## profile de degisiklik yaptik. eger commit false demeden yapsaydik bu durumda bu profile in user i olmadan direkt db ye kayit yapacakti. 
            profile.save()

            login(request, user)
            return redirect("home")

    context = {
        "form_user" : form_user,
        "form_profile" : form_profile 
    }

    return render(request, "users/register.html", context)








def user_login(request):
    form = AuthenticationForm(request, data=request.POST or None)
    
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("home")
    
    return render(request, "users/login.html", {"form" : form})



## logout icin view yazmadik. urls.py import ettik hazir