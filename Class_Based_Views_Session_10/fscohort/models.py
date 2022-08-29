from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=30, db_column="name_first")
    last_name = models.CharField(max_length=50, help_text="Please Enter Your Last Name")
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    number = models.IntegerField()
    image = models.ImageField(upload_to = "student_foto/", default = "/static/fscohort/avatar.jpg")
    GENDER = (
        ("1", "Female"),
        ("2", "Male"),
        ("3", "Prefer Not Say")
    )

    gender = models.CharField(max_length=20, choices=GENDER, default="Prefer Not Say")

    def __str__(self):
        return f"{self.number} - {self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Studentsss"
        db_table = "number"



## Notes:

## blank form validation icindir. yani sadece ui tarafi ile ilgili db ile degil
## null ise verinin db deki yerinin bos olabilecegini söyler. null false ise bizi veri girmeye zorlar. 

## help_text kullandigimizda;  admin panel de o veriye ait input un altinda yardim metni cikar.

#  /img/default.jpg    -   Absolute Path (starts with slash)
#  img/default.jpg     -   Relative Path (doesn't start with slash)
## Önemli:  eger default bir image i user a static file dan  service etmek istersek, bu durumda absolute path yazmak zorundayiz. yukarida oldugu gibi

## Önemli:  static file ayarlamasi yaparken, settings.py da hersey hazir durumda ancak biz sadece urls.py da eklenti yapariz. 

## media url ayarlari ise biraz daha fazla:
# 1: main proje url ine ekleme yapilir 
# 2: settings.py media url eklenir
# 3: settings.py da media root eklenir 


#  Önemli:  django; user tarafindan eklenne fotolari otomatik olarak media diye bir klasör olusturur ve o klasör icine atar. ancak bizim upload_to diyerek olusturdugumuz klasör ise media klasörü icinde olusturulur ve yükledigimiz fotolar onun icine atilir. 

