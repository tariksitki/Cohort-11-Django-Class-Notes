from django.shortcuts import render

# Create your views here.

from rest_framework import generics, status
from users.serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token 


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all() ## burada da User yerine settings.py dan cektigimiz degiskeni yazma sansimiz var. 
    serializer_class = RegisterSerializer


    ## create yazma nedeni. signal ile olusturdugumuz token i user a return ettigimiz data icine bu token i da koymak.  bu create methodu ile front end e artik token i da gönderiyoruz. 
def create(self, request, *args, **kwargs):   ## source koddan aldik
        serializer = self.get_serializer(data=request.data)
        # if serializer.is_valid():
        #     sunu sunu yap 
        ## buradaki if yapisinin short cut i sudur: raise_exception
        serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)  souerce a bakarsan save islemi yapar burasi 
        user = serializer.save()
        data = serializer.data
            ## token normalde regioster da üretiliyor ama yine de kontrol ediyoruz. 
        if Token.objects.filter(user=user).exists():
            token = Token.objects.get(user=user) # istedigimiz token a ulas
        else:
            data["error"] = "User has not Token"
        data["token"] = token.key ## onun icine key i koy
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

## register url i ile register olduktan sonra user/auth/login/ uerl inde emailimiz ile giri yapiyoruz bize key dönüyor. o key ile her seferinde giris yapabiliyoruz. 
## bu key browser da attigimiz her istekte olmasi gerekir. ve postman de 
## logout da bu key silinir. 
### sadece logout url ile istek yaptigimizda key silinir mi ? (arama cubuguna logout yazip deneyelim) postman de olur. 
## silinmez cünkü burada biz key göndermediugimiz icin django hangi user in logout olmak istedigini bilemez. 
## su an kullandigimiz paketin özelligi, logout oldugumuz da key otomatik silinir. normal de django default u silmez. 

## user register oldugunda create üretmemiz gerekir. Cünkü register olan kisi ayni anda login olsun istiyoruz. 
# bizim signals diye bir yapimiy var. Bir db de birsey gerceklestigi anda diger db de baska bir islem tetikleyebiliyoruz. register da biz data dönüyoruz. döndürdügümüz bu data icine bir de token i koyariz. Frontend bi token i alir ve bu token ile bizi istedigi yere yönlendirir. 

# eger bunu yapmazsak,  frontend register olan kisiyi login sayfasina redirect eder. login olmasini ister. 
# https://chrome.google.com/webstore/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj?src=modheader-com

## token return etme isini view de de yapabiliriz ama signals daha iyi bir yöntem 

## tüm bu islemleri yaptik ama su an user login oldugunda sadece key dönüyor front end e json olarak. Ama front end bizden user login oldugunda;  user a ait tüm datalar dönsün isteyebilir. 

## 
