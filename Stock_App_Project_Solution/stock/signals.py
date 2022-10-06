
## burada 2 islem olacak
##  quantity ile price i carp  toplam price olarak koy. 
## ve;  transaction in ise ilgili tabloya git ürünümü 1 artir. out ise tablomdan stogu 1 düsür.
## signal kullanma senbebimiz,  buradaki islemler verimiz db ye kayit edilmeden yapilmais gerekir. 

### buradaki logic leri burada yazmak zorundayiz. cünkü bir yerde islem oldugunda baska bir yerde baska modellerde tetikleme olsun istiyoruz. diger normal logic ler views.py da

from django.db.models.signals import pre_save  ## signal i yakalyacak olan sey
from django.db.models.signals import post_save  ## stock miktari degisince otomatik fiyat hesaplamasi iicn
from django.dispatch import receiver
from .models import Product, Transaction

@receiver(pre_save, sender = Transaction) 
def calculate_total_price(sender, instance, **kwargs):
    if not instance.price_total:  ## price yoksa sunu yapacak
        instance.price_total = instance.quantity * instance.price

## cok önemli:  bunun calismasi icin app.py da ready func yazdik. 






### stock sayisini azalttigimizda yada yükselttigimizde total price otomatik hesaplansin istiyoruz. 

@receiver(post_save, sender = Transaction)
def update_stock(sender, instance, **kwargs):
    ## ilk önce hangi product oldugunu belirliyourz. 
    product = Product.objects.get(id=instance.product_id)  # dbde product_id böyle gecer. 
    if instance.transaction == 1:
        if not product.stock: ## eger db de stock yoksa nulldir ve integer ile toplamak istedigimizde hata aliirz. istersek baslangic degeri olarak 0 da verebiliriz. 
            product.stock = instance.quantity
        else:
            product.stock += instance.quantity # db de stock varsa üzerine 1 ekle.

    else:
        product.stock -= instance.quantity ## peki burada neden if else yapisii kurmadik null ihtimaline karsi. Bunu serializer da handle edecegiz. 


### burasi db ile ilgili islmeler oldugu icin error mesaji dönemeyiz. O nedenle mesela stock da 6 tane var. ama user 10 tane istiyor. bu duurmda hata mesaji vermek icin  serializer kullnacaz ve buradaki degerin 0 in altina düsmeisini engellemis olacafiz. 