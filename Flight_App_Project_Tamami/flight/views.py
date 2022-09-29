from django.shortcuts import render

from flight.models import Flight, Reservation

# Create your views here.

from .serializers import FlightSerializer, ReservationSerializer, StaffFlightSerializer
from rest_framework import viewsets
from .permissions import IsStaffOrReadOnly
## sadece staff larin crete islemi yapmasi icin permissions.py da yazdigimiz kodu kullanacagiz buardaa

from datetime import datetime, date  ## eski yeni ucuslari hesaplamak iicn

class FlightView(viewsets.ModelViewSet):  ## modelviewset bizden iki veri bekler
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStaffOrReadOnly,)
    
        ## methodu overwrite ediyoruz. cünküstaff olanlar flight lari görürken icindeki reservationlari da görsün. normal user sadece flight lari görsün 
    def get_serializer_class(self):
        serializer =  super().get_serializer_class()
        if self.request.user.is_staff:
            return StaffFlightSerializer # kendimiz yazdik
        return serializer


    ## normal user lar sadece gelecek ucuslari staf ise bütün hepsini görsün. o nedenle buradaki queryset methodu overwrite edilir. bunun icin buflight modleindeki tarih ve saatler kullanilir. 
    def get_queryset(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S") # istedigimiz formata belirleriz. hour minute second
        today = date.today()

        if self.request.user.is_staff:
            return super().get_queryset()
        else:
            queryset = Flight.objects.filter(date_of_departure__gt=today)  ## docs da filter methoduna ait look up lara bakabiliriz. __ ile kullanilir. gt greater than demekti. bugünden büyük olanlari getir. büyük olanlari aldik simdi saate baktiracagiz. 
            if Flight.objects.filter(date_of_departure = today):
                today_qs = Flight.objects.filter(date_of_departure=today).filter(etd__gt = current_time) # yani tarihi bugün olanlarin saati su an dan büyük olanlar gelsin. Bunlari staff olmayanlar görecek. staff olanlar hepsini görecek. 
            queryset = queryset.union(today_qs) ## iki queryset i birlestiriyoruz. 
            return queryset
                


 
## modelviewset bizim icin ## get, post, update, delete   hepsini hallediyor. ancak urls de bunun icin router kullanilir. ayni endpoint le post put delete de yapilabilir ancak bu islmeler icin spesific bir id number ister bizden. 


## permission yazildiktan sonra; postman de istek yaparken header kisminda token imizi eklemek zorundayiz. aksi takdirde get de yapamayiz kimliksiz istek olmaz. admin panel de ii tane user olusturalim biri staff digeri degil. ikisinin yapabilecegi islemler farkli. 





class ReservationsView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    ## normal user lar sadece kendi rezervasyonlarini görsün staff ise hepsini. bunun icin souerce kod daki get_queryset methodu overwrite edilir. 

    def get_queryset(self):
        queryset = super().get_queryset()  ## inherit etiigimize ait olani al. 
        if self.request.user.is_staff:
            return queryset  ## bütün reservation lari al
        return queryset.filter(user=self.request.user) # sadece login olmus kisinin reservationlari gelsin. bu islmelerden sonra iki farkli user in token i ile istek atalim resv icin. biri staff olsun biri olmasin. 
        ## bu islemler ileri seviye islemler. 







