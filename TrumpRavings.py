from APIProxy import APIProxy
from Log import Log
import requests
from pprint import pprint


class TrumpRavings(APIProxy):
    def __init__(self):
        self.id = 2

        self.log_obj = Log()

        self.quotes = []
        self.url = ''
        self.quote = ''
        self.get_data()

    def get_data(self):
        for i in range(100):
            self.req = requests.get('https://api.tronalddump.io/random/quote')
            self.log_obj.get_log(self)

            pprint(self.req.headers)
            data = self.req.json()
            self.url = data['_embedded']['source'][0]['url']
            self.quote = data['value']
            pair = [self.url, self.quote]
            self.quotes.append(pair)
        return self.quotes
