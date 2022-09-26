from django.shortcuts import HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics

#### auth:

from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly


## öncelikle settings.py in en altinda kod yazdik 

# Create your views here.
def home(request):
    return HttpResponse('<h1>API Page</h1>')

    ## get ve post:

class StudentList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
        ## 1. auth:
    ##### artik auth olmayan birisi create ve get yapamaz. auth olmayan birisi bu view i calistiramaz. 
    # permission_classes = [IsAuthenticated] ## bu basic auth.. bunu kullanmak icin önce settings.py da kod yazdik en altta. bu view i kullanmak icin her istekte username ve password göndermek gerekir. Bu nedenle postman de auth kisminda bu verileri yaziyorz. url degismiyor sadece ekstradan bu iki bilgi gönderilir. bu view bizim login olmamizi ister. ister admin panelde login olup istek atabiliriz. yada postman de username ve password yazarsak o zaman bizi login olmus kabul eder. 
    # bu bilgileri göndermek icin postman de; authorization kismina girilip type secilir. 

        ## 2. auth
    permission_classes = [IsAdminUser]  ## sadece login olmak yeterli degil. ayni zamanda admin olmak gerekir. postman de de admin olan kisinin username ve password unu göndermemiz gerekir. 

        ## 3. auth:
    permission_classes = [IsAuthenticatedOrReadOnly]  # eger login degilse sadece okuyabilsin, post yapamasin. 



#! IsAuthenticated 👉 A user who is not logged in cannot make get and post requests.
#! IsAdminUser 👉 Only an admin user can make a get and post requests.
#! IsAuthenticatedOrReadOnly 👉 If the user is not logged in, he/she can only make a get request.





       
    ## update delete read:

class StudentOperations(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()