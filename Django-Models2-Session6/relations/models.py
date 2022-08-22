

from django.db import models


class Creator(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        ## burada last name basa alinirsa language tablosunda da o sekilde cikar 

    def __str__(self):
        ordering = ["first_name"]

# one2one relation:


class Language(models.Model):
    name = models.CharField(max_length=50)
    creator = models.OneToOneField(Creator, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.creator}"


# on_delete properties:

    # CASCADE -> if primary deleted, delete foreing too.
    # SET_NULL -> if primary deleted, set foreign to NULL. (null=True) olmak zorunda
    # SET_DEFAULT -> if primary deleted, set foreing to DEFAULT value. (default='Value") olmak zorunda 
    # DO NOTHING -> if primary deleted, do nothing.
    # PROTECT -> if foreign is exist, can not delete primary. foreign varsa pri silmez




## many2one :

class Framework(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"{self.name} - {self.language}"

    class Meta:
        ordering = ["name"]