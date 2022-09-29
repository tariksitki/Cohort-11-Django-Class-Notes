
# sadece staff personein create islemi yani flight üretmesini istiyoruz. 

from rest_framework import permissions

class IsStaffOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: ## get, head, options yöntemleri. yani veri okumaya yarayan methodlar veri de degisiklik yapmaz. 
            return True
        return bool(request.user and request.user.is_staff)


## IsAdminUser  bu sadece admin user lara izin verir. ama biz bunu biraz degistirecegiz. 
## source kodunda has_permission methodunu alip custom edecegiz. 

## if request.method in permissions.SAFE_METHODS:  burada in olacak == olmali. 

