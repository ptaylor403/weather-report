import json
import requests
from zipcode import Zipcode
from search_url import Url

key = 'dcbb6477fb1a29d2'
base_url = ("http://api.wunderground.com/api/{}/".format(key))
data = 'geolookup/conditions/forecast10day/alerts/currenthurricane/astronomy/pws:0/q/'


def main():
    zipcode = Zipcode.get_zip()
    url = Url.create_url(zipcode)
    # r = requests.get(lookup_url)
    # r_json = r.json()
    # for key, value in r_json.items():
    #     print(key)

main()
