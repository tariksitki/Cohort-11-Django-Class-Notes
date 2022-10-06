from random import choices
from django.db import models

# Create your models here.

from django.contrib.auth.models import User

## abstract model: benzer fiedl inheritance
# .. birden cok yerde kullanacagimiz seyleri abstart olarak kullaniriz. 

## frontend de görmek istedigimiz herseyi burada hayal edip ekleyebiliriz. 


## abstarct:  bu tarihler hepsinde kullanildigi icin
class UpdateCreate(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    class Meta:
        abstract = True  ## django ya bunun bir abstarct oldugunu söylüyoruz.




## en üst catidan basliyoruz:
## name icinde abstract yazilabilir. name de cogu yerde var

class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name



class Brand(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name





### product lari tutttugumuz asil tablo:
## UpdateCreate  zaten models den  inherit edilir. Product da onlari almi olur. 

class Product(UpdateCreate):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = "products")  ## istersek many many olabilir. yani bir ürün birden cok category de olsun denebilir. önce onetomany belirleyip many many ye gecersek cok sikinti olur. yapilmaz degil yapilir ama mesakkatli
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE, related_name = "b_products") ## bunun ismi de products olabilir. bir ürünün birden cok markasi olabil 
    stock = models.SmallIntegerField(blank=True, null=True) ## db de cok yer kaplamasindiye

    def __str__(self):
        return self.name

    

## ürünleri aldigimiz firma ismi. asagida yazilan transaction modelinde hangi firma ile calisildigimnin belli olmasi iicn yaziyoruz. hayal edebiliriz. su firmadan su kadar mal aldik. parasinin su kadari aldi verildi su kadari kaldi gibi yapilabilir. 
class Firm(UpdateCreate):
    name = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 15)  ## bu integer field da olabilir.
    address = models.CharField(max_length = 200)

    def __str__(self):
        return self.name



## null olayi cok önemli. özellikle integer larda neyin null olup olmayacagini belirlememiz gerekir. eger db ye integer alanina null gelirse program tamamen calismayi durdurur. string lerde zaten default olarak gelir cok problem olmaz. 

class Transaction(UpdateCreate):
    TRANSACTIONS = (
        ("1", "IN"),
        ("O", "OUT"),   ## bu veriler backend icin 0 ve 1 olarak da tutulabilir. 
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) ## islemi hangi user in yaptigi önemli bir kayit. setnull da null true zorunludur. user silindiginde user silinsin ama transaction silinmesi kalsin daha sonra kayitlardan bakalim. 
    firm = models.ForeignKey(Firm, on_delete = models.SET_NULL, null=True, related_name="transactions") ## transaction yapilan firma
    transaction = models.SmallIntegerField(choices=TRANSACTIONS) ## 2 secenek oldugu icin ayri bir tabloya gerek yok. in ve out. Bu veriyi user dan frontend de istedigimiz gibi alabiliriz. integer olarak yada char field olabilir. burasi charfield dda olabilir bu udurmda maxlendght gerekir. 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = "transaction") ## hanfi ürün ile ilgili transaction yapilmis. onu tutuyoruz ve product silinice kayiti tutmaya gerek yok diye siliyoruz. 
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2) # toplamda kac tane sayi alsin ve bunlardan kac tanesi decimal olsun
    price_total = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.transaction} - {self.product} - {self.quantity}"


##  Modelimize ürün fiyatını belirlemek için price alanını düşünelim. Fiyatlar ondalık sayılardan oluşmaktadır. 10 lira 25 kuruş gibi. Ondalık sayılar için Float Field ve Decimal Field kullanılan alan tipleridir. Bunların ana farkı Float Field küçük sayıları ile Decimal Fieldin daha büyük sayıları kabul etmesidir.Float Fieldin en fazla alabileceği basamak adedi 7 dir ve veritabanında 4 byte yer kaplar.Decimal Fieldin ise alabileceği en fazla basamak 29 dur. Veritabanında 16 byte yer kaplar. Decimal Fieldın diğer bir farkıda basamak sayısının ve ondalık kısımın sınirlandırılabilir olmasıdır. Decimal Field max_digits ve decimal_places argümanlarını alır. max_digits maksimum izin verilen basamak sayısıdır. decimal_places ise kullanılacak ondalık basamak sayısıdır. decimal_places, max_digits'den büyük olamaz.
