

class UserLog:
    def get_log(self, obj):
        with open('user.log', 'a') as file:
            #ToDo Add info for file header
            data = obj.req.headers['Date'] + " | " + obj.req.headers['Set-Cookie'][91:120] + "\n"
            file.write(data)


class TrumpLog:
    def get_log(self, obj):
        with open('trump.log', 'a') as file:
            #ToDo Add info for file header
            data = obj.req.headers['Date'] + " " + obj.req.headers['Server'] + " " + obj.req.headers['Connection'] + "\n"
            file.write(data)


class SunLog:
    def get_log(self, obj):
        with open('sun.log', 'a') as file:
            #ToDo Add info for file header
            data = obj.req.headers['Date'] + " " + obj.req.headers['Server'] + " " + obj.req.headers['Connection'] + "\n"
            file.write(data)


class Log:
    def __init__(self):
        self.user_log = UserLog()
        self.sun_log = SunLog()
        self.trump_log = TrumpLog()

    def get_log(self, obj):
        if obj.id == 0:
            self.user_log.get_log(obj)
        if obj.id == 1:
            self.sun_log.get_log(obj)
        if obj.id == 2:
            self.trump_log.get_log(obj)
