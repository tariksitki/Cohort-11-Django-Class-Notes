from tabnanny import verbose
from django.db import models

# Create your models here.

## Model class i yaklasik 2000 satirdan olusur.

class Student(models.Model):
    ## burada belirledigimiz max_length ler büyük projelerde önemli. cünkü db de buna göre yer ayirir
    ## id field i olusturmadik. otomatik yapar ve bunu primary key yapar.
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField()
    description = models.TextField(blank=True, null=True) # parantez ici bos olursa o zaman default olarak required olur. 
    register_date = models.DateField(auto_now_add=True) # bu sadece tarih alir. 
    ## auto_now_add=True dedigimizde bu class dan instance olusturdugumuzda otomatik atar
    last_update = models.DateTimeField(auto_now=True)  # hem tarih hem saat
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return (f"{self.number} - {self.first_name}")

    def student_year_status(self):
        "Returns the student's year status."
        import datetime
        if self.register_date < datetime.date(2019, 1, 1):
            return "Senior"
        elif self.register_date < datetime.date(2020, 1, 1):
            return "Junior"
        else:
            return "Freshman"

    class Meta:
        ordering = ["number"]
        verbose_name_plural = "Student_List"
        db_table = 'Student_List'
        ## ordering ve verbose db de degisiklik yapmaz. db_tables yapar

## auto_now_add=True  auto_now=True   farki:
## update olunca auto_now
## auto_now_add=True  ise create ederken bir kere alir. 

## python manage.py makemigrations
## ben bir model olusturdum. ve python a diyorum ki sen gerekli hazirliklarini yap. 

## migrate komutu ile de ilgili tablo db de ayaga kaldirilir.


# Django migration ları denilince akla ilk olarak veritabanı şemasını doğrudan etkileyen kavramlar gelir. Bir modele yeni bir alan eklemek, bazı alanların özelliklerini değişen ihtiyaçlara göre değiştirmek vs. Django bu değişiklikleri takip eder, migration dosyaları oluşturur, uygular ve veritabanınızı kolayca yeni şemasına geçirmenize yardımcı olur.
# Bunun yanında migrationlar varolan şema içersindeki verileri düzenlemek veya taşımak için de kullanılabilir. Bu tip migrationlar data migrations olarak adlandırılır. Şemayı ilgilendirmedikleri için Django tarafından takip edilmezler, geliştirici tarafından oluştururlar fakat normal şema migrationları gibi yürütülürler ve sistemin bir parçasıdırlar. Bu yazıda data migrationlarını bir örnek üzerinden inceleyeceğiz.


## olusan migrate dosyasini inceleyelim. 

