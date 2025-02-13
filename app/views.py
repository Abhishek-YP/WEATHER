from django.shortcuts import render

import requests
# Create your views here.

def apicall(url):
    return requests.get(url).json()
def home(request):
    city=request.GET.get('city', 'bangalore') 
    api_key='babf5215ce21dd3a8c23d63c35ea905d'
    api_key2='E2_Zb2FUxKVesaqWkkWp4VFLSC7-TwyvCIvj698YJfA'
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    url2=f'https://api.unsplash.com/search/photos?query={city}&client_id={api_key2}&per_page=1'
    api = apicall(url)
    api2 = apicall(url2)

    temperature =api['main']['temp']
    windspeed = api['wind']['speed']
    humidity=api['main']['humidity']
    name=api['name']
    country=api['sys']['country']
    icon=api['weather'][0]['icon']
    weather=api['weather'][0]['main']
    description=api['weather'][0]['description']
    if 'results' in api2 and len(api2['results']) > 0:
        city_image = api2['results'][0]['urls']['regular']  # Get first image
    else:
        city_image = ""

    img_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"

    

    

    ##https://api.openweathermap.org/data/2.5/weather?q=mandya&appid=babf5215ce21dd3a8c23d63c35ea905d&units=metric
    
    return render(request,'index.html',{'temperature':temperature, 'windspeed':windspeed, 'humidity':humidity, 'name':name, 'country':country,'img_url':img_url ,'weather':weather, 'description': description, 'city_image':city_image})
