from flask import Flask, render_template
import requests
from urllib.request import urlopen
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch location data
    locURL = 'https://ipinfo.io/json'
    location = urlopen(locURL)
    YourLoc = json.load(location)
    cityName = YourLoc.get('city')

    # Fetch weather data
    apiKey = '98943b1b4b2021db6e7a9f14cb07059b'
    baseURL = 'https://api.openweathermap.org/data/2.5/weather?q='
    completeURL = baseURL + cityName + '&appid=' + apiKey
    response = requests.get(completeURL)
    data = response.json()

    # Extract weather data
    temp = float(data['main']['temp']) - 273.15
    feels_like = float(data['main']['feels_like']) - 273.15
    max_temp = float(data['main']['temp_max']) - 273.15
    min_temp = float(data['main']['temp_min']) - 273.15

    # Extract location data
    location_data = {
        'Your IP': YourLoc.get('ip'),
        'Your City': YourLoc.get('city'),
        'Your Region': YourLoc.get('region'),
        'Your Country': YourLoc.get('country'),
        'Your Location': YourLoc.get('loc'),
        'Your Wifi': YourLoc.get('org'),
        'Your Postal': YourLoc.get('postal'),
        'Your Time Zone': YourLoc.get('timezone')
    }

    # Render the HTML template with data
    return render_template('index.html', temp=temp, feels_like=feels_like, max_temp=max_temp, min_temp=min_temp, location_data=location_data)

if __name__ == '__main__':
    app.run(debug=True)
