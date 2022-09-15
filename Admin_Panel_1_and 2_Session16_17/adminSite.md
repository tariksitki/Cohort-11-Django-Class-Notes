### PRECLASS SETUP

```bash
# CREATING VIRTUAL ENVIRONMENT
# windows
py -m venv env
# windows other option
python -m venv env
# linux / Mac OS
python3 -m venv env

# ACTIVATING ENVIRONMENT
# windows
.\env\Scripts\activate
# linux / Mac OS
source env/bin/activate

# PACKAGE INSTALLATION
# if pip does not work try pip3 in linux/Mac OS
pip install django
# alternatively python -m pip install django

python -m django --version
django-admin startproject core .

pip install python-decouple
pip freeze > requirements.txt
```
add a gitignore file at same level as env folder

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

go to terminal, stop project, add app

```
py manage.py startapp products
```

go to settings.py and add 'products' app to installed apps 


---------------------------------------------------------------------------------------------------
admin panel hemen hemen her projede vardir. cünkü auth islemleri buradan gerceklesir. 

products/models.py

```python
from django.db import models
## ürünün detayina ulasmak icin /id koyairz. ama user bu id yi görmesin diye her bir ürün icin unique bir slug olusturulur. Bunu django da slugField yapar. 

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
	is_in_stock = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
    
    def __str__(self):
        return self.name
```

* makemigrations and migrate
* createsuperuser

products/admin.py

```python
from django.contrib import admin
from .models import Product

admin.site.register(Product)

admin.site.site_title = "Clarusway Title"
admin.site.site_header = "Clarusway Admin Portal"  
admin.site.index_title = "Welcome to Clarusway Admin Portal"
```

Add data with Faker package
fake ürün bilgileri gimek icin kullanilir. 
https://faker.readthedocs.io/en/master/


* pip install Faker

tek tek el ile veri girmek yerine istedigimiz kadar veri üretebiliriz. 
asagida yazan islemleri normal views.py dan da yapabiliriz ama shell den daha basit. 

py manage.py shell
go to shell:
```bash
from product.models import Product
from faker import Faker
faker = Faker()

for i in range(1,200):
	product = Product(name=faker.name(),description=faker.paragraph(),is_in_stock=False)
	product.save()
```

product.save() dememek icin product.objects.create kullanabiliirz. 

go to admin site and check data (verileri görebilmek icin, admin panel de products tablosuna tiklamamiz gerekir.)


-------------------------------------------------------------------------------------------------

### ModelAdmin options and methods

modelAdmin:
got to django admin site document and modelAdmin source 


some modelAdmin options:
asagidaki kodlar admin.py da

```python

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "is_in_stock", "update_date")
    list_editable = ( "is_in_stock", )
    # list_display_links = ("create_date", name) hangi veriler üzerinde link olsun istersek o verileri tuple icine yazariz.  
    # #can't add items in list_editable to here
    ## yani üzerinde tiklanacak link olan degerler edite edilemez. tiklama ile edit karismasin diye.  ama yine degistirmek istersek readonly_fields = ("bring_image",) kullanilir. 
    list_filter = ("is_in_stock", "create_date")
    ordering = ("name",)  
    search_fields = ("name",) # bir tane input getirir admin panele. arama icin
    prepopulated_fields = {'slug' : ('name',)}   # when adding product in admin site
    list_per_page = 25
    date_hierarchy = "update_date" ## action in altinda bir tarih bölmesi cikarir. Bu tarihler arasinda oklar ile gezeriz. 
    # fields = (('name', 'slug'), 'description', "is_in_stock") # ayni tuple icinde olanlari yan yana koyar. 
    # #fieldset kullandığımız zaman bunu kullanamayız

    fieldsets = (
        (None, {
            "deneme": (
                ('name', 'slug'), "is_in_stock" # to display multiple fields on the same line, wrap those fields in their own tuple
            ),
            # 'classes': ('wide', 'extrapretty'), wide or collapse
        }),
        ('Optionals Settings', {
            "classes" : ("collapse", ),
            "fields" : ("description",),
            'description' : "You can use this section for optionals settings"
        })
    )



admin.site.register(Product, ProductAdmin)

```

actions section:
```python

   actions = ("is_in_stock", )

   def is_in_stock(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f"{count} çeşit ürün stoğa eklendi")
        
   is_in_stock.short_description = 'İşaretlenen ürünleri stoğa ekle'
```

Add methods to modelAdmin:


```python
from django.utils import timezone

		list_display = ("name", "create_date", "is_in_stock", "update_date", "added_days_ago")    
	
	    def added_days_ago(self, product):
        	fark = timezone.now() - product.create_date
        	return fark.days
```


-----------------------------------------------------------------------------------------------------




### RichText Editors (Description yazarken daha güzel bir editör)
    WYSIWYG (what you see is what you get)

    https://djangopackages.org/grids/g/wysiwyg/
    https://django-ckeditor.readthedocs.io/en/latest/

* pip install django-ckeditor

* 'ckeditor',      >>> add installed_apps

models.py
```Python
    from ckeditor.fields import RichTextField

    description = models.TextField(blank=True) >>>> description = RichTextField()
```

* makemigrations and migrate

* for extra config go to settings.py

settings.py
```Python
    CKEDITOR_CONFIGS = {
        'default' : {
            'toolbar' : 'full',
            'height' : 700,
            'width' : 1000
        }
    }

    büyüklük ayarlari degistirilebilir. 
```
* Note: ilgili template dosyasında: {{description | safe}}




-----------------------------------------------------------------------------------------------------





### Model Relations 

* Add new model:

models.py
```python
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    is_released = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"{self.product.name} - {self.review}"  
```

* makemigrations and migrate

admin.py
```Python
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 50
    raw_id_fields = ('product',) 

admin.site.register(Review, ReviewAdmin)
```

asagidaki kod, her bir product icin 4 tane yorum üretir. yani 199 x 4 tane review olur. 
shell
```
from product.models import Product, Review
from faker import Faker
faker = Faker()
for product in Product.objects.iterator():
    reviews = [Review(review=faker.paragraph(), product=product) for _ in range(0,4)]
    Review.objects.bulk_create(reviews)

Review.objects.count()
```

### TabularInline
Birden cok tabloyu bir sayfada gösterme saglar. 
yani bir ürüne ait 4 yorum var. her bir yorum icin bir field acar. extra 1 dedigimiz icin 1 tane daha acar. 

admin.py
```Python
class ReviewInline(admin.TabularInline):  # StackedInline farklı bir görünüm aynı iş
    '''Tabular Inline View for '''
    model = Review
    extra = 1
    classes = ('collapse',)
    # min_num = 3
    # max_num = 20


class ProductAdmin(admin.ModelAdmin):
    inlines = (ReviewInline,)
```

### custom fields

models.py
```Python
class Product(models.Model):        

    def how_many_reviews(self):
        count = self.reviews.count()
        return count
```

* add productAdmin >>> list_display ("how_many_reviews")



### horizontal & vertical filter (ManytoMany Field)
yukarida yaptigimiz islemler onetomany icindi. 
Burada ise manytomany iliskili iki tablonun ayni admin panel de gösterilmesi


models.py
```Python
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="category name")
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name

class Product(models.Model):
    ...
    categories = models.ManyToManyField(Category, related_name="products")
```

* makemigrations and migrate

admin.py
```Python
from .models import Product, Review, Category

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
    filter_horizontal = ("categories", )
   # filter_vertical = ("categories", )

admin.site.register(Category)
```





# Display Image Fields

product in detay sayfasinda foto gösterme: 

settings.py
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles'),
]
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

url.py
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

slug: SEO dostu link gibi düşünebiliriz. Örnek: apple-iphone-13-blue-123

models.py
```python
from django.utils.safestring import mark_safe

product_img = models.ImageField(null=True, blank=True, default="defaults/clarusway.png", upload_to="product/")

    def bring_image(self):
        if self.product_img:
            return mark_safe(f"<img src={self.product_img.url} width=400 height=400></img>")
        return mark_safe(f"<h3>{self.name} has not image </h3>")

## bring_image bize image in html kodunu return eder. Bu kodu da admin panel de fields icine koyariz ve ekrana yazdiririz. 
## mark safe,  baskalari bizim kodumuza sizip script ler calistirabilir. Bu nedenle django html kodu göndermeye izin vermez kendi iicnde. eger göndereceksek de bu sekilde göndermemizi ister. 
## self.product_img.url  hangi object ile is yapiyorsak onun img url i demek 
```
Bu islemleri source koduna girip yapabilirdik ama birisi bizim kodumuzu indirdiginde env klasörü gelmez. Bu nedenle bizim degisikliklerimiz gelmemis olur. 

* pip install pillow
* makemigrations and migrate

admin.py
```python
readonly_fields = ("bring_image",)

    fieldsets = (
        (None, {
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
```



listede image gösterme:
Önemli:
Bir methodu model de bir methodu admin de olusturduk. model de olusturdugumuz methodlari o modelin bir field i gibi projenin diger taraflarinda kullanabiliyoruz. Ancak admin.py da yazarsak sadece admin panel ile ilgili. Sadece admin panel de kullanacagimiz seyleri model de yapmaya  gerek yok. model de olusturacagimiz field lar icin self kullanilir. yani o object e ait. 
modelde kullandigimiz field lari admine tasimak istersek model de self yazdigimiz yerleri orada obj seklinde yaziyoruz.   adminde paranterz icinde (self, obj) yazariz. self.img yerine obj.img yazilir. 



admin.py
```python
from django.utils.safestring import mark_safe
	list_display = ("name", "create_date", "is_in_stock", "update_date", "added_days_ago", "how_many_reviews", "bring_img_to_list")    

    def bring_img_to_list(self, obj):
        if obj.product_img:
            return mark_safe(f"<img src={obj.product_img.url} width=50 height=50></img>")
        return mark_safe("******")
    
    bring_img_to_list.short_description = "product_image"
    ## ürün icine girerek foto degistirebiliriz. 
```

--------------------------------------------------------------------------------------









# Customize templates

admin panel de bir django template idir. ve bunu customize edebiliyoruz. 

default directory : env/lib/django/contrib/admin/templates/admin
template ler burada yatar. degsiiklik yapacagimiz zaman bu dosyalara gidip orada yapmiyoruz. Cünkü env icinde kalir ve baskasi kullanamaz. o nedenle asagidaki sekillerde yapiyoruz. 

    admin panel de gördügümüz sayfalarin isimleri su sekildedir: Hangi sayfada degisiklik yapacagizi buradan görebiliriz: 

    ## admin panelde en cok kullandigimiz sayfalar:
Liste Sayfası -> admin/change_list.html
Ekleme ve Güncelleme Sayfaları -> admin/change_form.html
Silme İşlemi İçin Onay Sayfası -> admin/delete_confirmation.html
Modelin Geçmişi -> admin/object_history.html (Bir product da degisiklik yaptiysak o degisiklikler bu sayfada bulunur.)

Daha detayli degisiklikler icin döküman incelenebilir. 

    ## customize edilecek template ler icin asagidaki hiyerarsi izlenmeli: 
admin/<extend_edilecek_sablon_adi>.html     >>>>>>> admin site ana sayfa
admin/<app_adi>/<extend_edilecek_sablon_adi>.html   >>>>>>>>> applere özel
admin/<app_adi>/<model_adi>/<extend_edilecek_sablon_adi>.html  >>>>>>>>>> modellere özel (mesela product lara özel detay sayfasi degisecek ise.)


settings.py:
```python
'DIRS': [BASE_DIR, "templates"],
```
normal de önce buraya bakmaz ama bu kod ile ilk buraya bakar. ilk önce buraya bakar yoksa defaulta gider,

ana dizinde su klasörler olusturulur: 
templates/admin/products(app ismi)/product(model ismi)/change_form.html

** içi boş olduğu için Ekleme ve Güncelleme Sayfaları boş görünecek

** default olan change_forma gidip blockları bakabiliriz istediğimizi güncelleriz extend edip
```html
orijinal olani extend ederiz. 
{% extends 'admin/change_form.html' %}

{% block form_top %}
    <h1>Product model new template</h1>
{% endblock  %}
```

daha fazla alan degistirmek istersek bu sayfanin orijinaline gideriz orada istedigimiz block u alip customize edebiliriz. degistirmedigimiz alanlari orijinalden alir. digerleri bizimkiler olur. 

-----------------------------------------------------------------------

admin templates extends hierarchy: (isleyis su sekildedir. Biz change_form dan extend ettik o baska yerden o baska yerden) Biz direkt base_site i da extend edebiliriz. 

base.html > base_site.html > change_form.html

    ana dizindeki klasörde su dosyalar olusturulur: 
templates/admin/base_site.html (direkt admin altina, herhangi bir app altina degil)

img directory :  contrib/admin/static/admin/img/clarusway.png
add clarusway.png to this directory

settings.py
## ana dizindeki static klasörü icindeki static resimlere bak demek
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles'),
]

base_site.html
```html
{% extends 'admin/base.html' %}
{% load static %}


{% block branding %}
    <div class="myDiv">
    <img src="{% static 'admin/img/clarusway.png' %}" style="height: 50px; width: 50px;" alt="">
    <h1 id="head">
        Clarusway Admin Site
    </h1>
    </div>
{% endblock %}
{% block extrastyle %}
    <style>
        #header {
            height: 50px;
            background: #542380;
            color: #fff;
        }

        #branding h1 {
            color: #fff;
        }

        a:link,
        a:visited {
            color: #10284e;
        }

        div.breadcrumbs {
            background: #542380;
            color: #10284e;
        }

        div.breadcrumbs a {
            color: #333;
        }

        .module h2, .module caption, .inline-group h2 {
            background: #542380;
        }

        .button, input[type=submit], input[type=button], .submit-row input, a.button {
            background: #10284e;
            color: #fff;
        }
        div.myDiv {
            display: flex;
            align-items: center;
        }

    </style>
{% endblock %}
```

Bunlari ögrenmek icin bol bol template ler ile oynayacagiz. eger bozarsak calismazsa env silip yeniden calistiracagiz. 





## Piyasada 150 $ a kadar django template ler satilir. 

Bu değiştirilmiş bir django admin sayfasıdır -> https://spruko.com/demo/django/noa/Noa/HTML/index.html
Google: django admin themes


# THIRD PARTY PACKAGES
daha cok sayida var bakabiliriz: 

### List-Filter Dropdown

* https://github.com/mrts/django-admin-list-filter-dropdown
bu sayfayi inceleyelim. dropdown var charfield var relatedfield lar icin özellikleri var. biz dropdown kulllandik 


    # bu ayri birsey third party olmadan :
product_admin da list_filter = ("is_in_stock", "create_date") satiri eklenir. istedigimiz alana göre filtreleme yapar.  Güzel bir özellik ama buraya name eklersek 199 tane isim filtrelemeye girer ve hos görünmez. kullanissiz oldu. Bu nedenle bunu third party kullandik .
######




## Bu da dropdown olarak filtre saglar. yani third party package ile filter ekler. 
pip install django-admin-list-filter-dropdown

INSTALLED_APPS = (
    ...
    'django_admin_listfilter_dropdown',
    ...
)

admin.py
```python
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 50
    list_filter = (
        ('product', RelatedDropdownFilter),
    )
```




## Kendimiz bastan sona django admin panel dizayn et ve github a yükle. mülakatta arz et. 




### Django admin date range filter
## ekranin sag üstünde date ve time ile filter saglar: 



https://github.com/silentsokolov/django-admin-rangefilter

* pip install django-admin-rangefilter

INSTALLED_APPS = (
    ...
    'rangefilter',
    ...
)

admin.py
```Python
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter# modelimizde hangisini kullandi isek

class ProductAdmin(admin.ModelAdmin):
    list_filter = ("is_in_stock", ("create_date", DateTimeRangeFilter)) # modelde datetimefield kullandığımız için
```






### import - export

## önemli verilerimizi import yada export etmeye yarar. sag üst kösede farkli formatlarda verilerimizi import export etme secenegi. 

## biz import export u review de yaptik . istersek product ve digerlerinde de yapabiliriz. 

## burada ayarlar var:
https://django-import-export.readthedocs.io/en/latest/

* pip install django-import-export

INSTALLED_APPS = (
    ...
    'import_export',
)

create resources.py (product app altinda bu dosya olustur.) 
```python
from import_export import resources
from product.models import Review

class ReviewResource(resources.ModelResource):

    class Meta:
        model = Review # default all fields
        # fields = ("is_released", "product")    
```

admin.py
```python
from import_export.admin import ImportExportModelAdmin
from product.resources import ReviewResource

    ## ReviewAdmin inherit ettigimiz yer degisecek.  artik buradan ImportExportModelAdmin
class ReviewAdmin(ImportExportModelAdmin):

    resource_class = ReviewResource
```










### custom template (grapelli):
## Grapelli sadece bir template. baska template lerde var. istersek bulabiliriz. 

templates for django interface diye aranabilir. Django packages diye sayfa var orada bulunabilir. free olanlar da var bir tanesini deneyelim nasil kullanilir. 

## Komple sayfanin görüntüsünü degistirir. Ancak foto felan ekledigimiz icin css de biraz sikintilar oldu. Bunlari customize edilebilir. 

https://django-grappelli.readthedocs.io/en/latest/

* pip install django-grappelli

    en üstte olmali 
INSTALLED_APPS = (
    'grappelli',    # en üstte olacak
    'django.contrib.admin',
)


    main.urls 
from django.conf.urls import include
urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS üstte olacak
    path('admin/', admin.site.urls), # admin site
]



