
from rest_framework import serializers
## model serializer kullanacagiz. o nedenle modelleri cagiriyoruz. 
from .models import Flight, Passenger, Reservation, User

## amacimiz json formatinda verileri görebilmek. bunun icin view yazmamiz gerekir. view yazabilmek icin  serializer yazmamiz gerekir. 


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = (   ## list de olabilir
            "flight_number",
            "operating_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd",
        
        )
        # normal personel sadece ucuslari görsün. staff ise ucuslar icinde reservationslari da görsün istiyoruz. bu nedenle flight serializer icine reservation serializer i da yazariz ama bunun icin ayri bir serializer yazariz. staffflightserializer


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"




class ReservationSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer(many = True, required=False) ## frontend e giden json daha anlamli olmasi icin bunu yaptik. 
    flight = serializers.StringRelatedField() ## bu islemi yaptigimizda flight tablomuzun str in da ne bulunuyorsa bize onu döndürüyor. bunu kullanmanin eksi bir yani var. create ederken bu alana ucus ismi yazarak create yapamayiz. sadece read only dir. bu nedenle flight_id olusturduk. bununla create edecegiz. yani get yaparken bu isim ile getie ama create ederken is ile create et. user icinde aynisini yapacagiz. 
    flight_id = serializers.IntegerField(write_only=True)
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(write_only=True, required=False)
    ## false cünkü asagida istegi atan userdan bu veriyi aliyoruz. 
    class Meta:
        model = Reservation
        fields = (
            "id",
            "flight",  # GET icin kullanilir
            "flight_id",  # POST icin kullanilir. 
            "user",  # GET
            "user_id",  # POST
            "passenger"
        )
        ## sadece bu veriler ile anlamli bir veri gönderemiyoruz frontend e o nedenle degisiklik yapacagiz. bunun icin önce passenger serializer yaziyoruz. sonra bu class icinde passenger degiskenine atiyoruz. bu islemleri yapmadan önce json veri icinde sadece passenger larin id numarasi dönüyordu. frontend baktiginda hicbirsey anlamiyordu. 

        ## buraya gelen veriler reservation tablosunda kaydedilmek üzere geliyor ama biz passenger a ait verileri alip onlari passsenger tablosuna kayit etmek istiyoruz. o nedenle pop ile alacagiz onlari. create methodunu overwrite edecegiz. 

    def create(self, validated_data):
        passenger_data = validated_data.pop("passenger")
        validated_data["user_id"] = self.context["request"].user.id  ## yani o anda kim login olmus ise o user i aliyoruz ve datamizin icine atiyoruz. frontend den user_id gelmesini beklemiyoruz. kendimiz otomatik aliyoruz. normalde view de request.user deyip aliyorduk ama serializer da bu sekilde alinir.  
        reservation = Reservation.objects.create(**validated_data) 
        ## yani reservation tablosuna passenger bilgisini passenger tablosunda kaydet geri kalan veri ile bu tabloda kaydet dedik. 

        for passenger in passenger_data:
            pas = Passenger.objects.create(**passenger)
            reservation.passenger.add(pas) # yani iki tabloda ayri ayri kayit yaptik. her bir tablonun ilgili verisini kendisine kaydettik. en son da bu iki tablonun verilerini birbirine bagladik add ile.  
        reservation.save()
        return reservation 




## swagger da methodlara tiklayarak hangi method da hangi veriyi göndermemiz gerekir görürüz. 

## postman de token göndermek icin Token yazip bosluk birakip token i yapistiriyoruz. 

##  





class StaffFlightSerializer(serializers.ModelSerializer):
    reservation = ReservationSerializer(many=True, read_only=True)  ## flight create ederken reservation create edilmeyecegi icin read_only yaptik. bunu yaptik ama view in haberi yok. ekleyelim. flightView de bir method overwrite edecegiz. 
    class Meta:
        model = Flight 





## reservation create edebiliyoruz ama update icin birsey yapmadik. ödev olarak yapali. 
## normal user lar sadece kendi reservation lari update edebilsin. 