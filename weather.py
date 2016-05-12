import json
import requests
from zipcode import Zipcode
from search_url import Url
from response import *
from ten_day import TenDay

key = 'dcbb6477fb1a29d2'
base_url = ("http://api.wunderground.com/api/{}/".format(key))
data = 'geolookup/conditions/forecast10day/alerts/currenthurricane/astronomy/pws:0/q/'


def main():
    zipcode = Zipcode.get_zip()
    url = Url.create_url(zipcode)
    response = Response.json_response()


    #10 day forecast
    day1 = TenDay.get_day1(response)
    print(day1)

    day2 = TenDay.get_day2(response)
    print(day2)

    day3 = TenDay.get_day3(response)
    print(day3)

    day4 = TenDay.get_day4(response)
    print(day4)

    day5 = TenDay.get_day5(response)
    print(day5)

    day6 = TenDay.get_day6(response)
    print(day6)

    day7 = TenDay.get_day7(response)
    print(day7)

    day8 = TenDay.get_day8(response)
    print(day8)

    day9 = TenDay.get_day9(response)
    print(day9)

    day10 = TenDay.get_day10(response)
    print(day10)


    #current conditions
    current = response['current_observation']
    location = current['display_location']['full']
    print('You are looking at the weather for {}'.format(location))
    time = current['observation_time']
    print(time)
    temp = current['temperature_string']
    print("\nTemperature: {}".format(temp))
    feels_like = current['feelslike_string']
    print("Feels like: {}".format(feels_like))
    clouds = current['weather']
    print(clouds)
    humidity = current['relative_humidity']
    print("With a humidity of {}".format(humidity))


    #sunrise and sunset
    sunset = response['sun_phase']['sunset']
    hour = sunset['hour']
    minute = sunset['minute']
    print("\nSunset will be at {}:{}".format(hour, minute))

    sunrise = response['sun_phase']['sunrise']
    hour = sunrise['hour']
    minute = sunrise['minute']
    print("Sunrise will be at 0{}:{}".format(hour, minute))


    #current alerts
    alert = response['alerts']
    if len(alert) == 0:
        print("\nNo severe weather reports at this time.")
    else:
        print("\nSevere weather reports in your area: {}".format(alert))


    #hurricane information

main()

# r = requests.get(lookup_url)
# r_json = r.json()
# for key, value in r_json.items():
#     print(key)
