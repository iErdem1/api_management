from APIProxy import APIProxy
import requests
from Log import Log
from User import User
from pprint import pprint


class Sun(APIProxy):
    def __init__(self, user_object=None):
        self.id = 1
        self.log_obj = Log()
        self.user_object = user_object
        self.user_object = User()
        self.results = []
        self.coords = []
        self.urls = []

        self.url_base = 'https://api.sunrise-sunset.org/json?lat={}&lng={}'

        self.get_coordinates(self.coords)
        self.create_urls(self.urls, self.coords)
        self.get_data(self.urls)

        pprint(self.results)
        pprint(self.coords)
        pprint(self.urls)

    def get_coordinates(self, coords):
        for i in range(len(self.user_object.users)):
            lat = self.user_object.users[i]['Latitude']
            lon = self.user_object.users[i]['Longitude']
            coords.append({'Lat': lat,
                           'Lon': lon})
        return coords

    def create_urls(self, url_list, coords):
        for i in range(len(coords)):
            url = self.url_base.format(coords[i]['Lat'], coords[i]['Lon'])
            url_list.append(url)
        return url_list

    def get_data(self, url_list):
        for i in range(len(url_list)):
            self.req = requests.get(url_list[i])
            pprint(self.req.headers)
            self.log_obj.get_log(self)
            data = self.req.json()
            res = data['results']
            self.results.append(res)
        return self.results

