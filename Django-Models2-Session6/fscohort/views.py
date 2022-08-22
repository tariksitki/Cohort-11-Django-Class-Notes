from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# terminalbir python ortami bu nedenle print yazilabilir. 
## node.js bizim react kodlarimizi calistiran bir motor 
## server ortamin da python sadece bir motor bu nedenle print kullanamayiz http response kullaniirz. 


def home(request):
    return HttpResponse("Hello welcome")

def fscohort(request):
    return HttpResponse("Hello from Fs Cohort")


def subfolder(request):
    return HttpResponse("Hello from Fs Cohort Subfolder")



#from http.client import HTTPResponse