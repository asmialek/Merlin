"""
Module is using OpenWeatherApi, from home.openweathermap.org.
"""

import pyowm
import datetime
import googletrans

# Todo: Google location translate


class WeatherSynapse(object):
    def __init__(self):
        self.api_key = '4f98b6ad217df75186d8e3fb52b7a9a8'
        self.owm = pyowm.OWM(API_key=self.api_key,
                             language='pl')
        self.trans = googletrans.Translator()
        # self.forecast_dict = {}

    def get_weather(self, location, date_and_time):
        location = self.trans.translate(location, dest='en').text
        if location[:2] == 'in':
            location = location[3:]
        if date_and_time.date() == datetime.date.today():
            return self.get_weather_today(location)
        elif date_and_time.date() > datetime.date.today():
            return self.get_weather_at_day(location, date_and_time)

    def get_weather_today(self, location):
        observation = self.owm.weather_at_place(location)
        weather = observation.get_weather()
        status = weather.get_detailed_status()
        temp = weather.get_temperature(unit='celsius')
        temp_avg = temp['temp']
        temp_min = temp['temp_min']
        temp_max = temp['temp_max']
        print(status, temp_avg, temp_min, temp_max)
        return status, temp_avg, temp_min, temp_max

    def get_weather_at_day(self, location, date_and_time):
        # Todo: Check if forecast already exists
        fc = self.owm.three_hours_forecast(location)
        f = fc.get_forecast()
        weather = fc.get_weather_at(date_and_time)
        status = weather.get_detailed_status()
        temp = weather.get_temperature(unit='celsius')
        temp_avg = temp['temp']
        temp_min = temp['temp_min']
        temp_max = temp['temp_max']
        print(status, temp_avg, temp_min, temp_max)
        return status, temp_avg, temp_min, temp_max


if __name__ == '__main__':
    ws = WeatherSynapse()
    loc = 'Warszawie'
    dt = datetime.datetime(2018, 4, 3, 12)
    # date_and_time = datetime.datetime(2018, 4, 2, 12)

    ws.get_weather(loc, dt)
    # ws.get_weather_at_day(location, date_and_time)
