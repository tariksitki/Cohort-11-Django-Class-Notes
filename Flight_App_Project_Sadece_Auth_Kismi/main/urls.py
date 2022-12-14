"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Three modules for swagger:
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

    ## drf yasg hem prod da hem de dev de kullanilir. Bu nedenle base.py da tanimlanir. 
    ## buradaki hali temel bir app icin yeterli. docs ile gelistiriilebilir. 

schema_view = get_schema_view(
    openapi.Info(
        title="Flight Reservation API",
        default_version="v1",
        description="Flight Reservation API project provides flight and reservation info",
        terms_of_service="#",
        contact=openapi.Contact(
            email="rafe@clarusway.com"),  # Change e-mail on this line!
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path("admin/", admin.site.urls),
    # Url paths for swagger:
    path("swagger(<format>\.json|\.yaml)",
         schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0),
         name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc",
         cache_timeout=0), name="schemaredoc"),
            ## debug toolbar:
    path('__debug__/', include('debug_toolbar.urls')),
        ## Bunu yaptiktan sonra swagger ekraninin saginda bir tus gelir. o tusa tiklayinca ekranin saginda debug ekrani acilir. eger acilmazsa browser F12 ye basilir. network e girilir ve burada cache deactivate yapilir. 
    path("users/", include("users.urls")),
    
]

# if DEBUG:
#     path('__debug__/', include('debug_toolbar.urls')),
# bu sekilde bir kullanimda var. yani debug == true ise demek. yani dev ortaminda isek 

