
'''
The purpose of this module is to give weather of location by the function getweather().
'''

from weather_location import Location
from weather_object import Weather
from weather_exeptions import WeatherRequestError as WeatherRequestError
from requests import get

url = 'http://api.openweathermap.org/data/2.5/weather'


def getweather(location, units='c'): # O(n)
    '''
    Gets weather of location. 

    The temperature units will be: "c" or "celsius" for Celsius, "f" or "fahrenheit" for Fahrenheit everything else will give the units Kelvin.
    '''
    params = {'id': location.id, 'appid': 'fdecc9b45b1a02f306b9af2ea3d6911f'}

    units = units.lower()
    if units in ['c', 'celsius', 'f', 'fahrenheit']:
        params['units'] = 'metric' if units in ['c', 'celsius'] else 'imperial'

    response = get(url, params=params).json()
    if int(response['cod']) != 200:
        raise WeatherRequestError(response['message'])

    del response['cod']
    return Weather(temp=response['main']['temp'], units='Celsius' if units in ['c', 'celsius'] else 'Fahrenheit' if units in ['f', 'fahrenheit'] else 'Kelvin', **response)