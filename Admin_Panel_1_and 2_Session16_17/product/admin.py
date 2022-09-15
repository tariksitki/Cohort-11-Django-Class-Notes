from django.contrib import admin

from product.models import Product, Review, Category
from django.utils import timezone
from django.utils.safestring import mark_safe
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter# modelimizde hangisini kullandi isek

from import_export.admin import ImportExportModelAdmin
from product.resources import ReviewResource


# Register your models here.

## link ve edit isleminin beraber kullanilmasi icin 



## tarayici daki sekme nin basligi
admin.site.site_title = "Clarusway Title"  

## admin panel ana baslik
admin.site.site_header = "Clarusway Admin Portal"

## ana baslik altindaki baslik
admin.site.index_title = "Welcome to Clarusway Admin Portal"




class ReviewAdmin(ImportExportModelAdmin):
    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 20
    raw_id_fields = ('product',)  # isimi degistiridim hata verdi deneyelim 

    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 50
    list_filter = (
        ('product', RelatedDropdownFilter),
    ) 
    resource_class = ReviewResource  ## import export icin. Review de yaptik sadece
    ## baska tablo ile baglantili oldugu icin RelatedDropdownFilter kullandik 

admin.site.register(Review, ReviewAdmin)


    # StackedInline farklı bir görünüm aynı iş, bunu da deneyelim. 
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
    prepopulated_fields = {'slug' : ('name',)} #isim ile baslayan slug olusturur. bu slug  a biz birde unique id ekleyerek kullanabiliriz. user görmemesi icin yapilir bu. unique id üreten generatorler var. Bu slug sadece admin panel icin gecerli. 
    list_per_page = 15
    date_hierarchy = "update_date"
    # fields = (('name', 'slug'), 'description', "is_in_stock")
    ## fields ve fieldsets ayni anda kullanilamaz. 
    readonly_fields = ("bring_image",)  ## product in foto lari icin
    def bring_img_to_list(self, obj):
        if obj.product_img:
            return mark_safe(f"<img src={obj.product_img.url} width=50 height=50></img>")
        return mark_safe("******")
    
    bring_img_to_list.short_description = "product_image"

        ## Bunu normal de model de yaptik burada yapmak istersek self yerine obj kullanilir. 
    # def bring_image(self, obj):
    #     if obj.product_img:
    #         return mark_safe(f"<img src={obj.product_img.url} width=400 height=400></img>")
    #     return mark_safe(f"<h3>{obj.name} has not image </h3>")

    fieldsets = (
        (None, {  ## isim 
            "fields": (
                ('name', 'slug'), "is_in_stock" # to display multiple fields on the same line, wrap those fields in their own tuple
            ),
            # 'classes': ('wide', 'extrapretty'), wide or collapse
        }),
        ('Optionals Settings', {
            "classes" : ("collapse", ),
            "fields" : ("description", "categories", "product_img", "bring_image"),
            'description' : "You can use this section for optionals settings"
        })
    )
    ## Optionals Settings alanini komple kopyalayip alta yapistirarak yeni alanlar ekleyebiliriz. ve bunun isimlerini istedigimiz gibi sekillendirebiliriz. 

        ### actions kismina parantez icinde yazdigimiz islemi ekler: kendimiz istedigimiz algoritmayi kurup acion ekleyebiliriz. 
    actions = ("is_in_stock", "is_out_stock")

    def is_in_stock(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f"{count} çeşit ürün stoğa eklendi")

    is_in_stock.short_description = 'İşaretlenen ürünleri stoğa ekle'

    def is_out_stock(self, request, queryset):
        count = queryset.update(is_in_stock=False)
        self.message_user(request, f"{count} çeşit ürün stoktan cikarildi")
    
    is_out_stock.short_description = 'İşaretlenen ürünleri stoktan cikar'


    list_display = ("name", "create_date", "is_in_stock", "update_date", "added_days_ago", "how_many_reviews", "bring_img_to_list")    
	
        ## önemli: Model de yada burada bir method yazabiliriz ve bunu bir field gibi kullanabiliriz. 
    def added_days_ago(self, product):
        fark = timezone.now() - product.create_date
        return fark.days
    ## hesaplama ile elde edilecek veriler db ye kaydedilmez. genel teamül böyledir. yani db de belki sadece ürünü alis tarihi tutulur.
    ## hesaplama yaptik sanki bir field mis gibi ekledik. 

    inlines = (ReviewInline,)
    ## yani icine girdigimiz product a ait review ler bu product a  girdigimizde bunun altinda görünür. ve bu product altinda düzenlenebilir. 

    # filter_horizontal = ("categories", )
    filter_vertical = ("categories", )

        ### güzel özellik. Parantez icinde yazdigimiz alanlara göre filtreleme saglar. 
    list_filter = ("is_in_stock", "create_date")

        ### Django admin date range filter
    list_filter = ("is_in_stock", ("create_date", DateTimeRangeFilter)) # modelde datetimefield kullandığımız için

    

### Productadmin i görebilmek icin su sekilde yazilir.
## python yukarıdan aşağı soldan sağa okur dip not
admin.site.register(Product, ProductAdmin)

admin.site.register(Category)


