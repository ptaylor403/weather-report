import json
import requests

key = 'dcbb6477fb1a29d2'
base_url = ("http://api.wunderground.com/api/{}/".format(key))
data = 'geolookup/conditions/forecast10day/alerts/currenthurricane/astronomy/pws:0/q/'
zipcode = input('\nPlease enter your zipcode: ')

if zipcode and len(zipcode) == 5:
    lookup_url = base_url + data + zipcode + '.json'
    print(lookup_url)
else:
    print("\nYou didn't enter a valid zipcode")

r = requests.get(lookup_url)
r_json = r.json()
for key, value in r_json.items():
    print(key)
