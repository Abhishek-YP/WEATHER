from django.shortcuts import render
import requests

def home(request):
    city = request.GET.get('city', 'bangalore') 
    api_key = 'b87770e0c526050cc7426cd23fa9cf28'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    api = requests.get(url).json()

    temperature = api['main']['temp']
    wind_speed = api['wind']['speed']
    humidity = api['main']['humidity']
    name = api['name']
    country = api['sys']['country']
    icon = api['weather'][0]['icon']
    weather = api["weather"][0]['main']
    description = api['weather'][0]['description']

    img_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"

    
    # https://api.openweathermap.org/data/2.5/weather?q=bangalore&appid=b87770e0c526050cc7426cd23fa9cf28&units=metric

    return render(request, 'index.html', {'temperature':temperature, 'wind_speed':wind_speed, 'humidity':humidity, 'name':name, 'country':country,'img_url':img_url, 'weather':weather, 'description':description})
