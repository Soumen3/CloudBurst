from django.shortcuts import render
from datetime import datetime
import requests
from geopy.geocoders import Nominatim
import os
from decouple import config

# Create your views here.


def home(request):
    context={}

    #--------------------Get the coordinates of the enterd city-------------#
    if request.method =='POST':
        city_name = request.POST['city']
        context['city']=city_name

        #----------get the coordinates--------------#
        coordinates = get_coordinates(city_name)
        if coordinates:
            latitude, longitude = coordinates
            context['lat']=latitude
            context['lon']=longitude
            

    #------------------------get the current location's coordinates-----------------------#
    else:
        current_location = get_current_location()
        if current_location:
            latitude, longitude, city_name= current_location
        # else:
            # print("Location information not available.")
        context['lat']=latitude
        context['lon']=longitude
        context['city']=city_name  


    #-------------------get the weather--------------------------#  


    # Retrieve the API key from an environment variable
    api_key = config("OPENWEATHERMAP_API_KEY")

    if api_key is None:
        raise Exception("API key not found in environment variables.")  
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"      # api url
    response = requests.get(url)
    data = response.json()      # get the data about weather

    kelvinTemp = data['main']['temp']
    celsiusTemp = kelvinTemp-273.15
    context['celsi']=round(celsiusTemp)
    feelsLike=data['main']['feels_like']-273.15
    context['feelsLike']=round(feelsLike)
    maxTemp=data['main']['temp_max']-273.15
    context['maxTemp']=round(maxTemp)
    minTemp=data['main']['temp_min']-273.15
    context['minTemp']=round(minTemp)
    humidity=data["main"]["humidity"]
    context['humidity']=humidity
    windSpeed=data["wind"]["speed"]
    context['windSpeed']=windSpeed
    direction=data['wind']['deg']
    context['direction']=direction
    pressure=data["main"]["pressure"]
    context['pressure']=pressure
    visibility=data['visibility']
    context['visibility']=visibility/1000
    sunriseTime=datetime.fromtimestamp((int)(data["sys"]["sunrise"])).strftime('%I:%M %p')
    context['sunrise']=sunriseTime
    sunsetTime=datetime.fromtimestamp((int)(data["sys"]["sunset"])).strftime('%I:%M %p')
    context['sunset']=sunsetTime

    cloudiness = data["clouds"]["all"]
    context['cloud']=cloudiness

    return render(request,'home.html', context)


def historicalData(request):
    return render(request,'historicalData.html')

def contact(request):
    return render (request,"contact.html")

def alert(request):
    return render(request,"alerts.html")

def about(request):
    return render(request,"aboutUs.html")









def get_coordinates(city_name):
    try:
        # Initialize a geolocator using Nominatim (OpenStreetMap)
        geolocator = Nominatim(user_agent="city_geocoder")

        # Use geocode to get location information for the city
        location = geolocator.geocode(city_name)

        if location:
            latitude = location.latitude
            longitude = location.longitude
            return latitude, longitude
        else:
            return None

    except Exception as e:
        return None


def get_current_location():
    try:
        # Make a GET request to the ip-api.com API
        response = requests.get('http://ip-api.com/json')

        if response.status_code == 200:
            data = response.json()
            latitude = data['lat']
            longitude = data['lon']
            city_name=data['city']
            return float(latitude), float(longitude), str(city_name)
        else:
            return None

    except Exception as e:
        return None

