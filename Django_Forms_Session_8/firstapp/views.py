from django.shortcuts import render, redirect

from firstapp.forms import StudentForm
from firstapp.models import Student

# Create your views here.


def index(request):
    return render(request, 'firstapp/index.html')

# def student_page(request):
#     return render(request,'firstapp/student.html')






# def student_page(request):
#     print(request.POST)  ## html de form da method post yaptik. burada image vermez
#     ## post un icine önce csrf token koyar sonra forms.py daki bilgileri 
#     print(request.FILES) ## image lar bu sekilde gelir 
#     form = StudentForm()
#     context = {
#         "form" : form
#     }

#     return render(request, "firstapp/student.html", context)



    ###  formun icini dolduruyoruz

# def student_page(request):
#     form = StudentForm()
#     if request.method == "POST":
#         form = StudentForm(request.POST, request.FILES)
#         if form.is_valid():
#             student_data = {
#                 "first_name" : form.cleaned_data.get("first_name"),
#                 "last_name" : form.cleaned_data.get("last_name"),
#                 "number" : form.cleaned_data.get("number"),
#                 "profile_pic" : form.cleaned_data.get("profile_image")
#             }
#             student = Student(**student_data) 
#             student.save()
#             return redirect("index")  ## urls.py da name e ne yazdiysak burada o yazilir.
#             # return redirect("student")  ## urls.py da name e ne yazdiysak burada o yazilir.
#     context = {
#         "form" : form
#     }

#     return render(request, "firstapp/student.html", context)


# db de profile_pic  olarak kayitli 
#  **student_data  bu kod :
## first_name=ali, last_name=veli gibi kodlari otomatik yazar


def student_page(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("student") ## formun icini bosaltarak ayni sayfayi verir
    context = {
        "form" : form
    }

    return render(request, "firstapp/student.html", context)
