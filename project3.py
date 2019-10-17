from Sun import Sun
from TrumpRavings import TrumpRavings
from User import User
from pprint import pprint

def main():
    pprint("asdasdsadasdasd")

    user_obj = User()
    sun_obj = Sun()
    trump_obj = TrumpRavings()

    for i in range(len(user_obj.users)):
        age = int(user_obj.users[i]['Age'])
        pprint("Welcome {name}!".format(name=user_obj.users[i]['Name']))
        pprint("""Here is your current location: {location} 
                    Sun Movement Information:
                    {sun_info}
                    According to your age, a silly Donald Trump tweet to have fun:
                    {trump}""".format(location=user_obj.users[i]['City'],
                                      sun_info=sun_obj.results[i],
                                      trump=trump_obj.quotes[age]))

if __name__ == '__main__':
        main()
