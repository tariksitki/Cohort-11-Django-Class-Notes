from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# def home_view(request):
#     html = "<h1> Hello From FirstApp </h1>"
#     return HttpResponse(html)


# def home_view(request):
#     print(request)
#     print("-------------")
#     print(request.method)
#     print("--------")
#     print(request.COOKIES)
#     print("--------")
#     print(request.path)
#     print("--------")
#     print(request.user)  ## bunun icin migrate komutu gereklidir. 
#     print("----------")
#     print(request.META)
#     html = "<h1> Hello From FirstApp </h1>"
#     return HttpResponse(html)


## csrf token oturuma has bize unique bir sifre atar. oturum esnasinda baskalarinin bizi taklit etmesini engeller. 




def home_view(request):
    ## db de bir tablo oluturup  ürünler = products.objects.all() deyip bunu context icine verebiliriz ve template de kullanabiliirz.
    print(request.path)

    context = {
        'title': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }
    return render(request, "firstapp/index.html", context)
