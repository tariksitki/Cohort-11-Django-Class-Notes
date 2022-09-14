from django.contrib import admin

from product.models import Product

# Register your models here.

## link ve edit isleminin beraber kullanilmasi icin 
# readonly_fields = ("bring_image",)


## tarayici daki sekme nin basligi
admin.site.site_title = "Clarusway Title"  

## admin panel ana baslik
admin.site.site_header = "Clarusway Admin Portal"

## ana baslik altindaki baslik
admin.site.index_title = "Welcome to Clarusway Admin Portal"


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "is_in_stock", "update_date")
    list_editable = ( "is_in_stock", ) # true isaretlersek save dememiz gerekir admin de

### Productadmin i görebilmek icin su sekilde yazilir.
## python yukarıdan aşağı soldan sağa okur dip not
admin.site.register(Product, ProductAdmin)



