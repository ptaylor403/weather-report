import json
import requests
from zipcode import Zipcode
from search_url import Url
from response import *

key = 'dcbb6477fb1a29d2'
base_url = ("http://api.wunderground.com/api/{}/".format(key))
data = 'geolookup/conditions/forecast10day/alerts/currenthurricane/astronomy/pws:0/q/'


def main():
    zipcode = Zipcode.get_zip()
    url = Url.create_url(zipcode)

    #current conditions
    current = Response.json_response()
    location = current['current_observation']['display_location']['full']
    print('\nYou are looking at the weather for {}'.format(location))
    time = current['current_observation']['observation_time']
    print(time)
    temp = current['current_observation']['temperature_string']
    print("Temperature: {}".format(temp))
    feels_like = current['current_observation']['feelslike_string']
    print("Feels like: {}".format(feels_like))
    clouds = current['current_observation']['weather']
    print(clouds)
    humidity = current['current_observation']['relative_humidity']
    print("With a humidity of {}".format(humidity))

    #10 day forecast
    forecast = Response.json_response()


    #sunrise and sunset
    sunset = Response.json_response()
    hour = sunset['sun_phase']['sunset']['hour']
    minute = sunset['sun_phase']['sunset']['minute']
    print("\nSunset will be at {}:{}".format(hour, minute))

    sunrise = Response.json_response()
    hour = sunrise['sun_phase']['sunrise']['hour']
    minute = sunrise['sun_phase']['sunrise']['minute']
    print("Sunrise will be at 0{}:{}".format(hour, minute))

    #current alerts

    #hurricane information

main()

# r = requests.get(lookup_url)
# r_json = r.json()
# for key, value in r_json.items():
#     print(key)
