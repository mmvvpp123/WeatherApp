from django.shortcuts import render
import requests

def home(request):
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?zip=10312,us&units=imperial&appid=5d01d42962323487bb4bf5293f529095')
    geodata = response.json()


    city_weather = {
        'city':geodata['name'],
        'temp':geodata['main']['temp'],
        'desc':geodata['weather'][0]['description'],
        'icon_id':geodata['weather'][0]['icon'],
        'wind_speed':geodata['wind']['speed'],
    }

    temp= geodata['main']['temp']

    return render (request, 'core/home.html', city_weather)
