from django.urls import path, include

from users.views import RegisterView


urlpatterns = [
        ## normalde böyle biz degistirdik
    # path('dj-rest-auth/', include('dj_rest_auth.urls'))
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', RegisterView.as_view(), name = "register"),
    ## register icin path yazdiktan sonra son islem olarak, base.py da basic auth yerine token auth olmasi iciin ayarlari yapiyoruz. Bu kodlari da rest api nin docs undan aldik. 
    

]