

## Buradaki kodlar models.py da da yazilabilir. ama bu best practice 

from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver 
from rest_framework.authtoken.models import Token 


@receiver(post_save, sender=User)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

    def ready(self):
        import users.signals  ## models.py da yazsaydik buna gerek yoktu. 


## Token modeli source kodunda user bulunur onu overwrite degistirdik
# signals naska yerde yazilinca ready yazilir
#  Bu signal yazdigimizda register  olduktan sonra direkt token olusturur. sonradan login olmaya gerek kalmaz eskiden login olunca üretiyordu.
## son olarak olsuturulan token i front end e göndermek icin view de ekleme yapacagiz. 
