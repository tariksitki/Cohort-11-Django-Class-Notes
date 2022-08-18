from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def secondHome(request):
    return HttpResponse("<h1>Hello world from Second App</h1>")