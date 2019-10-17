from APIProxy import APIProxy
from Log import Log
import requests
from pprint import pprint


class User(APIProxy):
    def __init__(self, user_number=10):
        self.id = 0
        self.users_raw_data = []
        self.users = []

        self.log_obj = Log()


        self.user_number = user_number
        self.get_data(self.user_number, self.users_raw_data)
        self.user_info(self.users_raw_data, self.user_number)


    def get_data(self, user_num, user_list):
        self.user_list = user_list

        for i in range(user_num):
            self.req = requests.get('https://randomuser.me/api/')
            self.log_obj.get_log(self)

            info = self.req.json()
            user_data = info['results']
            self.user_list.append(user_data)
        return self.user_list

    def user_info(self, users, user_num):

        for i in range(user_num):
            full_name = users[i][0]['name']['first'] + ' ' + users[i][0]['name']['last']
            dob = users[i][0]['dob']['date'][:10]
            age = users[i][0]['dob']['age']
            city = users[i][0]['location']['city']
            lat = users[i][0]['location']['coordinates']['latitude']
            lon = users[i][0]['location']['coordinates']['longitude']

            self.user = {'Name': full_name,
                         'DOB': dob,
                         'Age': age,
                         'City': city,
                         'Latitude': lat,
                         'Longitude': lon}
            self.users.append(self.user)
        return users


