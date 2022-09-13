from django.shortcuts import render
## pythonda api ye istek icin:  bunu önce install etmek gerekir.
import requests

### gelen veriyi daha güzel okumak icin:
from pprint import pprint

# apikey .env dosyasinda
from decouple import config

def index(request):
    API_KEY = config("API_KEY")
    city = "Yozgat"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    
    response = requests.get(url)
    content = response.json()  # json formatindaki veriyi python dict e dönüstürür
    print("---------------------")
    # print(response)
    # pprint(content)
    pprint(content["name"])  ## print ettigimizde görürüz bizim isimize bu veri yarayacak
    pprint(content["main"]["temp"])
    pprint(content["weather"][0]["description"])
    pprint(content["weather"][0]["icon"])


    return render(request, 'weatherapp/index.html')

