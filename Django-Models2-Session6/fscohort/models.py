from django.db import models

# Create your models here.


class Student(models.Model):
    COUNTRIES = [ 
        ("TR", "Turkey"),
        ("DE", "Germany"),
        ("FR", "France"),
        ("US", "America"),
    ]
    first_name = models.CharField("Adi", max_length=50)
    last_name = models.CharField("Soyadi", max_length=50)
    number = models.IntegerField("Numara")
    about = models.TextField("Hakkinda", blank=True, null=True)
    ## blank hic veri göndermeme null bos
    avatar = models.ImageField("Resim", upload_to = "media/", blank="True", null=True)
    registered_date = models.DateTimeField(auto_now_add=True)
    ## bana sormadan ben submit tusuna basinca o anin zamanini ekle 
    update_date = models.DateTimeField(auto_now=True)
    country = models.CharField("Ülke", max_length=2, choices=COUNTRIES)

    def __str__(self):
        return f"{self.number} - {self.first_name} - {self.last_name}"

    class Meta:
        ordering = ["-number"]  # DESC => ["-number"]



# db mizi güncellemke icin degisiklikleri yakalatmamiz lazim bunun icin de makemigrations komutu calisir. 
## yakalandiktan sonra migrate ile güncellenir. 


# django da class larin default degerleri vardir. bu default degerleri meta class i ile degistirebilirz. 

### veriyi ilk kayit esnasinda; update date e de tarih atamasi yapar. 

