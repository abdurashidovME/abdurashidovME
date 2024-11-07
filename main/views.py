import requests
from django.shortcuts import render
from django.utils import timezone


def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q=jizzakh&appid=a2611c36ac0bd0a6630b09f18e5668a6'
    city = 'Jizzakh'

    r = requests.get(url.format(city)).json()

    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],

    }

    context = {'city_weather': city_weather}
    return render(request, 'weather/index.html', context)
