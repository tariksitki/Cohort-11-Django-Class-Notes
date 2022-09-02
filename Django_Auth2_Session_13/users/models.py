from tkinter import CASCADE
from django.db import models

# Create your models here.
from django.contrib.auth.models import User


    ## bu bizim iki ayri tablo olusturdugumuz yöntem.

# class UserProfile(models.Model):
#     portfolio = models.URLField(blank=True)
#     profile_pic = models.ImageField(upload_to="profile_pics", blank=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     ## cascade: parent silinince child da silinir. 
#     def __str__(self):
#         return self.user.username 

#     class Meta:
#         verbose_name_plural = "User Profile"





### bu ise iki tabloyu birlestiriyoruz. bu nedenle ikinci tabloda kullanmak zorunda oldugumuz user ilk tabloda var oldugundan cekmeye gerek kalmiyor. 



from django.contrib.auth.models import AbstractUser

    ## burada modelimizi inherit ediyoruz üzerine polimorfism olarak ilave ediyoruz. 

class User(AbstractUser):
    portfolio = models.URLField(blank = True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)


# settings.py da bir ayar yapmamiz gerekiyor unutma. cünkü ana default tabloda bir degisiklik yaptik. 
# AUTH_USER_MODEL = 'users.User'



