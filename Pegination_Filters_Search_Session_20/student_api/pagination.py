
from rest_framework.pagination import PageNumberPagination

class SmallPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param="sayfa"  ## bunu yazinca url de yazacagimiz isim degisir
