from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


## max_length varchar gibi 
## __str__     objectlere human readable bir görünüm saglar

## pillow python a ait image library dir. 
## bu django ya has birsey degil. python la image kullanacak isek yüklemek zorundayiz

