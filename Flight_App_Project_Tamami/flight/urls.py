
from importlib.resources import path
from flight.views import FlightView, ReservationsView
### view de modelviewset kullandigimiz icin router kullaniyoruz. 
from rest_framework import routers


router = routers.DefaultRouter()
router.register("flights", FlightView)
router.register("resv", ReservationsView)

urlpatterns = [

]

urlpatterns += router.urls

### browser da http://127.0.0.1:8000/flight/flights/  yaziyoruz. 

## modelviewset bizim icin ## get, post, update, delete   hepsini hallediyor. ancak urls de bunun icin router kullanilir. ayni endpoint le post put delete de yapilabilir ancak bu islmeler icin spesific bir id number ister bizden. 

## router.register("flights", FlightView)  buradaki flights ile sadece  get olabilir.  
## slash koyup id number koyarsak diger islemlerde yapilabilir. 

## router baska neler icin kullanilir. arastiralim 

## ayni url ile postman de create de yaptik. 