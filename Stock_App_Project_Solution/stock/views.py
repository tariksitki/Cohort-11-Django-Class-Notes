from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, filters ### settings.py da ekleme yapilir. 
from django_filters.rest_framework import DjangoFilterBackend
from stock.serializers import BrandSerializer, CategorySerializer, FirmSerializer, ProductSerializer, TransactionSerializer
from .models import (
    Category,
    Brand,
    Firm,
    Transaction,
    Product
)



class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # filter_backends = [filters.SearchFilter]
    search_fields = ["name"]




class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'brand']
    search_fields = ['name']



## seach olayi cok genis. elastik serach var dinamyc search var arastiralim. 








class FirmView(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["name"] ## frontend de neye göre search edebiliriz. 






class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # hangisi in hangisi out görmek icin
    filterset_fields = ['firm', 'transaction', 'product']
    search_fields = ['firm']  # istedigimiz field eklenebilir.
    ## mevcut user kim ise onu aliyoruz. bunun icin en kolay yöntem su:
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
