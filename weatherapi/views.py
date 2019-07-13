from django.shortcuts import render
from .forms import ZipCode
import requests


def home(request):
    return render (request, 'core/home.html', {})

def weather(request):
    form = ZipCode(request.GET)

    zip= form['zip_code'].value()
    if zip == None:
        url_request = ('https://api.openweathermap.org/data/2.5/weather?zip=10312,us&units=imperial&appid=5d01d42962323487bb4bf5293f529095')
    else:
        url_request = ('https://api.openweathermap.org/data/2.5/weather?zip='+ zip + ',us&units=imperial&appid=5d01d42962323487bb4bf5293f529095')

    response = requests.get(url_request)
    geodata = response.json()

    city_weather = {
        'city':geodata['name'],
        'temp':geodata['main']['temp'],
        'desc':geodata['weather'][0]['description'],
        'icon_id':geodata['weather'][0]['icon'],
        'wind_speed':geodata['wind']['speed'],
    }

    temp= geodata['main']['temp']

    return render(request, 'core/weather.html', city_weather)
