
from django.http import HttpResponse

def firstapp(request):
    return HttpResponse("<h1>Hello From First App</h1>")