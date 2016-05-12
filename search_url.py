from zipcode import *

class Url(Zipcode):

    def create_url(zipcode):
        key = 'dcbb6477fb1a29d2'
        base_url = ("http://api.wunderground.com/api/{}/".format(key))
        data = 'geolookup/conditions/forecast10day/alerts/currenthurricane/astronomy/pws:0/q/'

        url = base_url + key + data + zipcode + '.json'
        print(url)
