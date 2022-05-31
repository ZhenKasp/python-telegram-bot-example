import os
import requests

from dotenv import load_dotenv

class OpenWeatherMap:
    def __init__(self):
        self.weather_api_key = os.getenv('WEATHER_API_TOKEN')

    def get_weather_by_coordinates(self, latitude, longitude, exclude = ''):
        return requests.get(url = f'https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude={exclude}&appid={self.weather_api_key}').json()

    def get_coordinates(self, city):
        return requests.get(url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limi  t=2&appid={self.weather_api_key}').json()

    def get_weather_by_city_name(self, city):
        return requests.get(url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={self.weather_api_key}').json()
