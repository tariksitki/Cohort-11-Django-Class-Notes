from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Flight(models.Model):
    flight_number = models.CharField(max_length = 20)
    operating_airlines = models.CharField(max_length = 50)
    departure_city = models.CharField(max_length = 30)
    arrival_city = models.CharField(max_length = 30)
    date_of_departure = models.DateField()
    etd = models.TimeField()  # estimated time of date

    def __str__(self):
        return f"{self.flight_number} - {self.departure_city} - {self.arrival_city}"

    ## parent tablo
class Passenger(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    phone_number = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



    ## child tablo
    ## bir user birden cok rezervasyon yapabilir ama bir rezervasyon birden cok kisiye ait olamaz bu nedenle foreign key kullandik user icin. yani one to many
    ## passenger icin:  yine bir yolcunun birden cok rezervasyonu olabilir. bir rezervasyonda birden cok yolcu olabilir. yani ben bir rezervasyonda kendim esim ve cocugum icin yapmis olabilirim. o nedenle passenger tablosu ile iliskiyi many to many yaptik. 
    ## rezervasyon flight iliskisi.  one to many. flight tablosundaki bir ucusa ait birden cok rezervasyon olabilir. ama tek bir rezervasyon hem ankara istanbul hem de ankara izmir olamaz. 
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    passenger = models.ManyToManyField(Passenger, related_name = "rezervations")
    flight = models.ForeignKey(Flight, on_delete = models.CASCADE, related_name="reservation")

    def __str__(self):
        return self.user 





## related_name = "rezervations" ;  rezervation tablosunda üretilmis olan bir rezervasyon objesinden parent tabloya ulasabiliyoruz. rezervations.passenger.all() diyerek. ama parent in haber yok. bu nedenle passenger.rezervations.all() diyerek related_name i kullanarak ulastik. 

## many to many de on delete belirtilmez. cünkü bir veri silindiginde ona ait baska veriler oluyor olacak. 

