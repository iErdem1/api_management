# from Log import Log
# from Sun import Sun
# from TrumpRavings import TrumpRavings
# from User import User
#
#
# class Display:
#     def __init__(self):
#         self.user_obj = User()
#         self.sun_obj = Sun()
#         self.trump_obj = TrumpRavings()
#         self.display()
#         print("asdlkjaslkdjaslkdjaslkdjalskjdlksadjlkasdjlks")
#
#
#     def display(self):
#         print("asdlkjaslkdjaslkdjaslkdjalskjdlksadjlkasdjlks")
#         for i in range(len(self.user_obj.users)):
#             age = int(self.user_obj.users[i]['Age'])
#             print("Welcome {name}!".format(self.user_obj.users[i]['Name']))
#             print("""Here is your current location: {location}
#                      Sun Movement Information:
#                         {sun_info}
#                      According to your age, a silly Donald Trump tweet to have fun:
#                         {trump}""".format(location=self.user_obj.users[i]['City'],
#                                           sun_info=self.sun_obj.results[i],
#                                           trump=self.trump_obj.quotes[age]))
