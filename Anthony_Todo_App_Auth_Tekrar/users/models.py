from django.db import models

# Create your models here.

from django.contrib.auth.models import User


    ### profile icin ikinci bir tablo olusturuyoruz. Bu tabloyu user tablosuna baglariz. alternatif olarak bu iki tabloyu tek tabloda birlestirebilirdik. Ama su an ki yöntem daha esnek. 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile_pics/", blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username  ####  Dikkat

    #   öenmli: buradaki blank ler olmayinca calismiyor. 



## bu yöntemde, template imizde iki formu alt alta basacagiz. 
# üstte username, email ve password  User modelinden gelecek.
# altta ise; bio ve picture;  Profile tablosundan gelecek. 

