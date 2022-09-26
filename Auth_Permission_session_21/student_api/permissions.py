

from rest_framework import permissions
    ## burada permissions.IsAdminUser class ini kendimize göre düzenleyecegiz.


    ## bu custom permission dir. Normal de yok biz yazdik. 

class IsAdminorReadOnly(permissions.IsAdminUser):
        ## views bazinda oldugu icin bu method overwrite edilir. 
    def has_permission(self, request):
        if request.method in permissions.SAFE_METHODS: # bilgide degisiklik yapmayan methodlar
            return True 
        else:
            return bool(request.user.is_staff)

    ## yani staff ise post yapabilecek. yoksa sadece read yapabilecek 


        ## simdi object seviyesinde permission yazacagiz:
        ### bunu projede kullanmadik. md dosyasi ile bunu koordine edelim .
        ## sadece bu objecti create eden kim ise onun yetkisi var. 
        ## object seviyesinde yazmak gercekten detay bir konu. ileri seviye bir konu

class IsAddedByUserorReadOnly(permissions.BasePermission):  
    def has_object_permission(self, request, view, obj):
        if request.method == permissions.SAFE_METHODS:
            return True
        else:
            return obj.user == request.user or request.user.is_staff