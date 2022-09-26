
## auth permission:

auth bizim kim oldugumuzu tespit eder. yetki kontrolü

permission ise;  bizim sahip oldugumuz gerekli izinleri düzenler. Bizim bir islemi yapmamiza yetkimiz var mi yok mu bunu kontrol eder. 

frontend in auth u atlatmasi biraz daha kolay. 

autentication kim oldugumuzu  authorization da permission gibi yetkilerimizi düzenler. 

hepsi rest framework docs da var. 

https://www.django-rest-framework.org/api-guide/permissions/

global de bir permission, yada localde view bazinda hatta sadece bir tablo üzerinde bir permission policy yapabiliriz. 

1: global settings.py da
2: views.py da view bazinda


class based view ise;  permission_class icinde
func based ise permission_classes   decoratörü icinde

bize built in gelen permission lar var:

allowany
isAuthenticated sadece kayit olmus lara aizin 
isAdminUser
isauthenticatedorreadonly

hepsi docs da detayli var. 

GET HEAD OPTIONS  bunlar sadece okuma yapabilen methodlar safe methods diye de gecer. 

object seviyesinde yani en özel seviyede permission vermek icin araya guardian diye paket ekliyoruz. 

Döküman cok güzel hazirlanmis. 

#####  
## autenticated policy miz best olarak globally olarak set edilir.  ve projemizin tüm kisimlari icin ayni olmasi iyi olur. 
## permissiion ise best olarak view bazinda set edilir. 


basic auth front end den yapilan her istekde istegi yapan kimse her istekte username ve password gönderilmek zorunda frontend tarafindan. genellikle testing icin uygundur.  cünkü her istekte bunlarin gönderilomesi güvenli degil. 
token auth
session auth

postman de sag tarafta beatufy tusu var. kodumuzu güzellestirir

postman de auth kismi var oradan izin seceiyoruz. 

basic auth u set etmek icin 
settings.py da en alta kod yazdik 
sonra view da IsAuthenticated i kullandik. 


    #! IsAuthenticated 👉 A user who is not logged in cannot make get and post requests.
    #! IsAdminUser 👉 Only an admin user can make a get and post requests.
    #! IsAuthenticatedOrReadOnly 👉 If the user is not logged in, he/she can only make a get request.


basic auth güvenli degil dedik. her istekte username ve password koymak iyi degil. 
birde bu  bizim passwordumuzu base 64 e göre hash ler. 
burada hashlenmis passwordu browser da base 64 decode dedigimizde cikan sitelerde direkt olarak cözümleyebilirler. 
bu nedenle sadece test de kullanilmasi tavsiye edilir. 



2:  token auth : 
frontend e bir token verilecek ve her seferinde bu token ile istek yapilir. 

token auth icin:
1: 'rest_framework.authtoken'    installed app e eklenir. 
2: migrate yapilir (token adinda tablo olustugu icin )
3: settings.py daki basic olan kodumuzu token yaptik 
4: Bundan sonra admin panel de token diye tablo olususr. 

admin panelde tokens a tiklayip admin user icin yada diger user lar icin token lusturduk. bu sekilde yetkileniyoruz. 
postman de istek yapmak icin headers kisminda;
key Authorization 
karsisina ise  Token 2b4321kj4b214kj21kj4j21   yazilir arada bosluk olmali.


react dan yapilan istek de username icin bir token üretiriz v bunu bir yerde saklariz. artik user her istek yaptiginda onun username i icin üretilen token i header kismina koyariz. 


signal:  bir islem yapildiginda baska bir islemi de pesine ekleyebiliyoruz. 
mesela bir create islemi oldugunda bu user a bir tane token olusturur. 
Bunun icin receiver decorator kullanilir. 
yani bir yerden sinyal geldiginde su isi yap diye bir tetikleyici. 


obtain token:
yeni app olusturduk user_api adinda
url lerini ayarladik 
login olacagiz frontend tarafindan. frontend e bir token verilir. sonrasinda hep bu token kullanilir. 
admin panelde yeni bir user üretiriz. bunun token i olamz. 
daha sonra postman de bu user in username ve passwordu ile istek atariz. Bu user icin token atar. ve bunu token tablosuna gittigimizde görürüz. Bu user logout oldugunda token silinir. 


register: 
user_api ye serializer ekliyoruz. 
özel serializer yaptik.  güzel, baska yerlerde kullanilabilir. 









# PRECLASS SETUP

```bash
# CREATING VIRTUAL ENVIRONMENT
# windows
py -m venv env
# windows other option
python -m venv env
# linux / Mac OS
vitualenv env

# ACTIVATING ENVIRONMENT
# windows
.\env\Scripts\activate
# linux / Mac OS
source env/bin/activate

# PACKAGE INSTALLATION
# if pip does not work try pip3 in linux/Mac OS
pip install django
# alternatively python -m pip install django
pip install python-decouple
pip freeze > requirements.txt
django-admin --version
django-admin startproject main .
```

## gitignore

add a gitignore file at same level as env folder, and check that it includes .env and /env lines

## Python Decouple

create a new file and name as .env at same level as env folder

copy your SECRET_KEY from settings.py into this .env file. Don't forget to remove quotation marks from SECRET_KEY

```
SECRET_KEY = django-insecure-)=b-%-w+0_^slb(exmy*mfiaj&wz6_fb4m&s=az-zs!#1^ui7j
```

go to settings.py, make amendments below

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
```

go to terminal

```bash
py manage.py migrate
py manage.py runserver
```

click the link with CTRL key pressed in the terminal and see django rocket.

## INSTALLING DJANGO REST

go to terminal

```bash
py manage.py makemigrations
py manage.py migrate
pip install djangorestframework
```

go to settings.py and add 'rest_framework' app to installed apps

## ADDING AN APP

go to terminal

```
py manage.py startapp student_api
```

go to settings.py and add 'student_api' app to installed apps

go to student_api.models.py

## ADDING MODEL

```python
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
```

go to student_api.admin.py

```python
from django.contrib import admin
from .models import Student

# Register your models here.
admin.site.register(Student)
```

## SERIALIZER FOR STUDENT MODEL

create serializers.py under student_api

```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ["id", "first_name", "last_name", "number"]
        fields = '__all__'
```

## SETING UP VIEWS

go to student_api.views.py

```python
from django.shortcuts import HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics

# Create your views here.
def home(request):
    return HttpResponse('<h1>API Page</h1>')

class StudentList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class StudentOperations(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

```

## SETING UP URLS

go to drf.urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('student_api.urls')),
]
```

go to student_api.urls.py

```python
from django.urls import path
from .views import home, StudentList, StudentOpr

urlpatterns = [
    path('', home),
    path('student/', StudentList.as_view()),
    path('student/<int:pk>/', StudentOpr.as_view(), name="detail"),
]
```

## RUNNING SERVER

```bash
py manage.py makemigrations
py manage.py migrate
py .\manage.py createsuperuser
pip freeze > requirements.txt
py .\manage.py runserver
```

## CORS SETUP

```bash
pip install django-cors-headers
```

settings.py

```python
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    # ...
    'corsheaders',
]
MIDDLEWARE = [
    # ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ...
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_EXPOSE_HEADERS = (
    'Access-Control-Allow-Origin: *',
)
```

# HANDS-ON PART

Permissions determine whether a request should be granted or denied access.

Authorization checks who sends this request.

## Permissions

### Setting the permission policy

The default permission policy may be set globally, using the `DEFAULT_PERMISSION_CLASSES` setting. For example.

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

You can also set the authentication policy on a per-view, or per-viewset basis, using the `APIView` class-based views.
**Example:**

```python
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
```

### Available Permissions

#### AllowAny

The AllowAny permission class will allow unrestricted access, regardless of if the request was authenticated or unauthenticated.

#### IsAuthenticated

The IsAuthenticated permission class will deny permission to any unauthenticated user, and allow permission otherwise.
This permission is suitable if you want your API to only be accessible to registered users.

#### IsAdminUser

The IsAdminUser permission class will deny permission to any user, unless user.is_staff is True in which case permission will be allowed.
This permission is suitable if you want your API to only be accessible to a subset of trusted administrators.

#### IsAuthenticatedOrReadOnly

The IsAuthenticatedOrReadOnly will allow authenticated users to perform any request. Requests for unauthorised users will only be permitted if the request method is one of the "safe" methods; GET, HEAD or OPTIONS.

#### DjangoModelPermissions

This permission class ties into Django's standard django.contrib.auth model permissions. This permission must only be applied to views that have a .queryset property or get_queryset() method.

#### DjangoModelPermissionsOrAnonReadOnly

Similar to DjangoModelPermissions, but also allows unauthenticated users to have read-only access to the API.

#### DjangoObjectPermissions

This permission class ties into Django's standard object permissions framework that allows per-object permissions on models.

## Authentication

### Setting the authentication scheme

The default authentication schemes may be set globally, using the DEFAULT_AUTHENTICATION_CLASSES setting. For example.

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```

You can also set the authentication scheme on a per-view or per-viewset basis, using the APIView class-based views.
Example

```python
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
```

## TokenAuthentication

This authentication scheme uses a simple token-based HTTP Authentication scheme. Token authentication is appropriate for client-server setups, such as native desktop and mobile clients.

In Basic Authentication you need to send always send username and password, in every request in headers. But this is not safe. To handle this issue token authentication was introduced. When a user logged in an authentication is sent as a response. After that in every request this token will be sent in heades instead of password and username.

These tokens should be stored in backend database. We have options to handle the this sequence. Most used case is to create a token when a user logged in and save it in db and then delete this token whenever user logged out.

To use the `TokenAuthentication` scheme you'll need to configure the authentication classes to include `TokenAuthentication`, and additionally include `rest_framework.authtoken` in your `INSTALLED_APPS` setting:

go to settings.py and add 'rest_framework.authtoken' into installed apps

```python
INSTALLED_APPS = [
    ...
    'rest_framework.authtoken'
]
```

go to terminal

```bash
py manage.py migrate
```

navigate to admin dashboard and check Token table

add users, and token to these users

go to postman send Token

## Adding an App for Authentication

## resgiter islemleri icin 
## Burada yapilan islemlerin bilgisi serializer ve views.py da var  user_api nin 

go to terminal

```bash
py manage.py startapp user_api
```

go to settings.py and add 'user_api' into installed apps

go to models.py

```python
from django.db import models

# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```

go to serializers.py

```python
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user

# from django.contrib.auth.models import User
# from rest_framework import serializers


# class RegistrationSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
```

go to main urls.py, and add following line into urlpatterns

```python

urlpatterns = [
    ...
    path('user/', include('user_api.urls')),
]
```

go to user_api urls.py

```python
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import  logout_view, RegisterView # ,registration_view

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    # path('register/', registration_view, name='register'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
]
```

go to views.py

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import status


# Create your views here.
# Registration with function based view
# @api_view(['POST'])
# def registration_view(request):
#     if request.method == 'POST':
#         serializer = RegistrationSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             password = serializer.validated_data.get('password')
#             # serializer.validated_data['password'] = make_password(password)
#             user = serializer.save()
#             user.set_password(password)
#             user.save()
#             # token, _ = Token.objects.get_or_create(user=user)
#             # data = serializer.data
#             # data['token'] = token.key
#         else:
#             data = serializer.errors
#         return Response(data)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        token= Token.objects.create(user=user)
        data = serializer.data
        data['token'] = token.key
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "created successfully", "details": data}, status=status.HTTP_201_CREATED, headers=headers)
  
@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        data = {
            'message': 'logout'
        }
        return Response(data)
```




## Custom Permission 

## Buradan asagisini buradan takip et dersi kacirdim. 
## dersin son yarim saatini tekrar dinleyelim 

## admin panel de user tablosunda user lara verdigimiz yetkilendirme object seviyesinde. biz ise burada studen seviyesinde yani daha detayli permission yazacagiz. 

custom yazmak iicn,, ya basepermission dan inherit edip onu overwrite edecegiz. yada view bazinda yazmak icin has_permission methodu
object bazinda yazmak icin has_object_permission methodu overwrite edilir. 

To implement a custom permission, override BasePermission and implement either, or both, of the following methods:
.has_permission(self, request, view)
.has_object_permission(self, request, view, obj)
The methods should return True if the request should be granted access, and False otherwise.

under student_api create permissions.py

```python
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user.is_staff)

class IsAddedByUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.user == request.user or request.user.is_staff
```

go to student_api models.py and make following amendments

```python
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
```

Here we added a new field as user which has one to many relation with User table. When we do migrations it will ask what do with current students in our db as they don't have any user currently. When asked you can type 1 and then press enter.

go to terminal

```bash
py manage.py makemigrations
py manage.py migrate
```

go to student_api views.py

```python
from django.shortcuts import HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from .permissions import IsAdminOrReadOnly, IsAddedByUserOrReadOnly
# from rest_framework.response import Response
# from rest_framework import status
# Create your views here.
def home(request):
    return HttpResponse('<h1>API Page</h1>')

class StudentList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    # authentication_classes = [BasicAuthentication]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        ## login olmus kimse onu perform ile create ediyoruz. 

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     if not serializer.is_valid(raise_exception=False):
    #         return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    #     serializer.validated_data['user'] = request.user
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response({"message": "created successfully"}, status=status.HTTP_201_CREATED, headers=headers)

class StudentOperations(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAddedByUserOrReadOnly]
```




# BONUS PART

## USING [ dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/index.html)

go to terminal

```bash
pip install dj-rest-auth
```

Add `dj_rest_auth` app to INSTALLED_APPS in your django settings.py:

```python
INSTALLED_APPS = (
    ...,
    'rest_framework',
    'rest_framework.authtoken',
    ...,
    'dj_rest_auth'
)
```

Add dj_rest_auth main urls:

```python
urlpatterns = [
    ...,
    path('auth/', include('dj_rest_auth.urls'))
]
```

Migrate your database

```bash
python manage.py migrate
```

## Registration (optional)

If you want to enable standard registration process you will need to install `django-allauth` by using `pip install 'dj-rest-auth[with_social]'`.

Add `django.contrib.sites`, `allauth`, `allauth.account`, `allauth.socialaccount` and `dj_rest_auth.registration` apps to INSTALLED_APPS in your django settings.py:

Add `SITE_ID = 1` to your django settings.py

```bash
INSTALLED_APPS = (
    ...,
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
)

SITE_ID = 1
```

Add dj_rest_auth.registration urls:

```bash
urlpatterns = [
    ...,
    path('auth/registration/', include('dj_rest_auth.registration.urls'))
]
```

Migrate your database

```bash
python manage.py migrate
```



## jwt token:

bunu arastiralim. ayri bir sifreleme olayi var. docs da third party auth da var. 

### dj-rest-auth paketini inceleyelim. 

## hson web token popüler arastiralim. 

