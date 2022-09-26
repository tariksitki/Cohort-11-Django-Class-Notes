from django.shortcuts import render
from .serializers import RegistrationSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token



### register icin view: 

## user bilgilerini alip cretae islemi yapacak.


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
        ## create methodunu source koda gidip aldik . resgiterolan kisinin token ini da üretmek icin overwrite edecegiz. 

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save() ## creata olan user icin token tablosunda üretim
        # token = Token.objects.create(user=user)  ## signal kullanmadan önceki hali 
        token = Token.objects.get(user=user) ## signalde üretildigi icin sadece cekme
        data = serializer.data
        data["token"] = token.key  # normalde token alani yoktu. 
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
## frontend ile konusulur bizden ne istiyorsa burada döndürülür. 
## bu view calistiktan sonra yeni bir user create edilir ve frontend e bilgileri döner. bilgiler icinde token bilgisi de olur. logout oldugunda token silinir. 

## signali models.py da yazdik. 



from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import status

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


## yeni user create etmek icin su bilgiler lazim 
## postman de bu bilgileri gönderince bize yeni bir user cretae eder. 

# {
#     "username": "Henry",
#     "password": "Murtaza66",
#     "password2" : "Murtaza66",
#     "email" : "test@test.com",
#     "first_name" : "henry",
#     "last_name" : "forester"

# }

## bu bilgileri postman de girmek bizim react da yaptigimiz islemlerdir. onu simule eder. 

## header kisina token konularak o istegin kimden geldigi bellli olur. 

## Bu bilgiler ile kayit yapan kisi icin yeni user register yaptik ama token üretmedik. iste bir user register oldugu zaman o kullanici icin token üretecegiz ve user a dönen data icin de gönderelim. bu islmeleri register yapan view de yapacagiz. 
## ve bu view in bir methodunu overwrite decegiz. 
# source koduna gidip bakalim . cretaeModelMixin den üretilir. yani create methodunu overwrite edecegiz. 







        #### logout:
        ## her loginde yeni bir token üretir o kullanici icin her logout da da siler token i 

@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        data = {
            'message': 'logout'
        }
        return Response(data)

## postman de calistirmak icin logout url yazilir. user bilgileri girilir. authorizatioon kisminin karsisina yine Token girilir. 
## bu islemden sonra token tablosuna baktigimizda o kisinin token ini siler. ve bu token ile giris yapmak istedigimizde hata aliriz. 

## hangi tip auth kullanacagimizi settings.py da belirledik.. base mi token mi.


