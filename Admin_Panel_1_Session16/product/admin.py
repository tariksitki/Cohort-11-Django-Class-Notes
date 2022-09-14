from django.contrib import admin

from product.models import Product, Review, Category
from django.utils import timezone

# Register your models here.

## link ve edit isleminin beraber kullanilmasi icin 
# readonly_fields = ("bring_image",)


## tarayici daki sekme nin basligi
admin.site.site_title = "Clarusway Title"  

## admin panel ana baslik
admin.site.site_header = "Clarusway Admin Portal"

## ana baslik altindaki baslik
admin.site.index_title = "Welcome to Clarusway Admin Portal"




class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 20
    raw_id_fields = ('product',) 

admin.site.register(Review, ReviewAdmin)


class ReviewInline(admin.TabularInline):  # StackedInline farklı bir görünüm aynı iş
    '''Tabular Inline View for '''
    model = Review
    extra = 1
    classes = ('collapse',)
    # min_num = 3
    # max_num = 20






class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "is_in_stock", "update_date")
    list_editable = ( "is_in_stock", ) # true isaretlersek save dememiz gerekir admin de
    # list_display_links = ("create_date", "name")
    search_fields = ("name",)
    prepopulated_fields = {'slug' : ('name',)} #isim ile baslayan slug olusturur. bu slug  a biz birde unique id ekleyerek kullanabiliriz. user görmemesi icin yapilir bu. unique id üreten generatorler var. 
    list_per_page = 15
    date_hierarchy = "update_date"
    # fields = (('name', 'slug'), 'description', "is_in_stock")
    ## fields ve fieldsets ayni anda kullanilamaz. 

    fieldsets = (
        (None, {
            "fields": (
                ('name', 'slug'), "is_in_stock" # to display multiple fields on the same line, wrap those fields in their own tuple
            ),
            # 'classes': ('wide', 'extrapretty'), wide or collapse
        }),
        ('Optionals Settings', {
            "classes" : ("collapse", ),
            "fields" : ("description", "categories"),
            'description' : "You can use this section for optionals settings"
        })
    )

        ### actions kismina parantez icinde yazdigimiz islemi ekler:
    actions = ("is_in_stock", "is_out_stock")

    def is_in_stock(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f"{count} çeşit ürün stoğa eklendi")

    is_in_stock.short_description = 'İşaretlenen ürünleri stoğa ekle'

    def is_out_stock(self, request, queryset):
        count = queryset.update(is_in_stock=False)
        self.message_user(request, f"{count} çeşit ürün stoktan cikarildi")
    
    is_out_stock.short_description = 'İşaretlenen ürünleri stoktan cikar'


    list_display = ("name", "create_date", "is_in_stock", "update_date", "added_days_ago", "how_many_reviews")    
	
    def added_days_ago(self, product):
        fark = timezone.now() - product.create_date
        return fark.days
    ## hesaplama ile elde edilecek veriler db ye kaydedilmez. genel teamül böyledir. yani db de belki sadece ürünü alis tarihi tutulur.
    ## hesaplama yaptik sanki bir field mis gibi ekledik. 

    inlines = (ReviewInline,)

    # filter_horizontal = ("categories", )
    filter_vertical = ("categories", )

    

### Productadmin i görebilmek icin su sekilde yazilir.
## python yukarıdan aşağı soldan sağa okur dip not
admin.site.register(Product, ProductAdmin)

admin.site.register(Category)


