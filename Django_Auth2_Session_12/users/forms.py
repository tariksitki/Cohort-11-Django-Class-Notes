
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django import forms 


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email") # password u django kendi halleder
        # fields = "__all__" ## burada all dersek admin panel deki user in tüm bilgileri  cikar


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # fields = "__all__"
        exclude = ("user",) # user i manuel girmememiz lazim. o nedenle bunu haric tuttuk
                            ## tuple olmali

        

