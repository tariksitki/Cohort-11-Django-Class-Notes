
from django.urls import path
from stock.views import BrandView, CategoryView, FirmView, ProductView, TransactionView
from rest_framework import routers

### modelviewset kullaninca router kullanmak zorundaiz. 

router = routers.DefaultRouter()
router.register("category", CategoryView)
router.register("brand", BrandView)
router.register("product", ProductView)
router.register("firm", FirmView)
router.register("transaction", TransactionView)

## default router kullandigimiz icin bize bir link return edecek ona tiklayinca  verilere gidecegiz

urlpatterns = [

] + router.urls

