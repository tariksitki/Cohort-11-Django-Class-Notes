
from rest_framework import serializers, validators  ##########
from django.contrib.auth.models import User 
## user modelini settings deki user dan cagirabiliriz daha dinamic bir yapi olur. 
## hazir validation yapisi:
from django.contrib.auth.password_validation import validate_password

    ## settings.AUTH_USER_MODEL   bunu burada kullanmak istersek:
# from django.conf import settings 
# User = settings.AUTH_USER_MODEL

## login olunca user a tüm verileri göndermek icin kullaniyoruz bunu. 
from dj_rest_auth.serializers import TokenSerializer

class RegisterSerializer(serializers.ModelSerializer):
        ## overwrite
    email = serializers.EmailField(
        required = True, ## source code a bakarsak blank true. biz simdi degistirdik. user giris yapmasi icin zorunlu olsun istiyoruz. 
        validators = [validators.UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password],
        style = {"input_type" : "password"}  ## browsable api deki görüntü
    )

    password1 = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password],
        style = {"input_type" : "password"} )

    class Meta:
        model = User ## bunu settings den import etmek icin, settings de AUTH_USER_MODEL diye bir degisken yazariz. Burada import ederiz ve settings.AUTH_USER_MODEL seklinde kullanitiz. zaten settings.py in default unda bu isimde degisken var. o nedenle burada model = User demek ise model= AUTH_USER_MODEL ayni seylerdir. birsey farketmez. sadece settings den cektigimizde daha dinamic bir yapi olusmus olur. 
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "password1",

        )

    ## password 1 ve 2 esit mi:
    def validate(self, data):  ## serializer icinde bize gelen data
        if data["password"] != data["password1"]:
            raise serializers.ValidationError(
                {"password" : "Password didn't match"}
            )
        return data

        ## register olunca user;  serilaizer icinde veriler bize gelecek. yukarida yazdigimiz field lerdeki veriler.  bu veriler ile simdi db de user create edecegiz. ancak password u hash lenmis sekilde gönderecegiz. bu islemleri yapabilmek icin create i tekrar yaziyoruz. 
        ## dict lerde pop ile silme islemi yapiyoruz. lsitelerde ise pop icine index no koymamiz lazim. Burada dict oldugu icin pop icine key ismi konulur. 
    def create(self, validated_data):  ## passwordler ayni ise bize validated data gelecek.
        password = validated_data.pop("password")  ## degiskene atiyoruz kullanacagiz.
        validated_data.pop("password1")  ## iki tane olmasin diye siliyourz
        user = User.objects.create(**validated_data) # tüm verileri icine koyup create
        user.set_password(password)  ## hash leme islemi
        user.save()
        return user 






## user moelinde emailler unique degil. zorunlu bir alan bile degil. username ise unique. biz user lari emailler ile register edecegiz. o nedenle overwrite edilir. 
## bunu ya user modelinde degisiklik ile yapariz. yada serializer da yapariz. 
## rest  docs da,  validators diye alan var. okuyalim . oradan kod aliyoruz email icin. 

## validation_password diyerek kendimiz customize edebiliriz ma her bir kriteri tek tek yazmak gerekir. if if elif diye..  bunun icin biz hazir kullanacagiz.  

## 



    ### login oldugunda sadece key dönüyordu. ama biz user in tüm verilerinin dönmesini istiyoruz. bu nedenle user  icin bir serializer olusutrduk. Burtadaki token serializer i overwrite ettik. Bu kismi videonun sonundan izleyelim. 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email"
        )


class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        fields = (
            "key",
            "user"
        )

## buradaki kodlara ilave olarak settings.py da da islem yaptik 
## tüm bu islemlerden sonra frontend tek bir istek ile key ve user a ait tüm bilgileri elde ediyor. ikinci bir istege gerek yok. 