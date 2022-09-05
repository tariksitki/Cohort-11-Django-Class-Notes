
from dataclasses import fields
from django import forms
from .models import UserProfile, User
from django.contrib.auth.forms import UserCreationForm



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("profile_pic", "bio")
        # exclude = ("user",)
        # field olarak hepsini cagirmadik. Cünkü modeldeki user kismi User tablosundan geliyor. eger burada user i da cagirirsak, db de kayitli olan herkesi getirecek. Bunu kime kaydediyoruz diyecek. Bize dropdown gibi birsey olusturacak. db de kayitli olan herkesi burada gösterecek. Bu da güvenli olmayan birsey. Biz ise girilen bilgilerin o anda formu dolduran kisiye kaydedilmesini istiyoruz. 


    ## neden bunu olusturuyoruz. user sadece username ve password girerek kayit olabiliyor. ama biz user dan baska bilgilerde girilmesini istiyoruz. o nedenle burada creation formu overwrite ederiz. password zaten yazsak da yazmasak da gelir. 

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")

