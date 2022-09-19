from django.db import models

# Create your models here.


# class Student(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     number = models.IntegerField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.last_name} {self.first_name}"
    
#     class Meta:
#         verbose_name = "Student"
#         verbose_name_plural = "Students"





    ## Relational fields (ögrencinin hangi path de oldugunu belirten bir durum var.)

    ## Bu modeli calistirmak icin db silinir. cünkü eski db ile yeniler uyusmuyor. 

class Path(models.Model):
    path_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.path_name}"    

class Student(models.Model):
    path = models.ForeignKey(Path, related_name='students', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"