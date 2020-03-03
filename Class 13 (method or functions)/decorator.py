# global var
LOGGED_IN = True
# LOGGED_IN = False

CREATED = True
# CREATED = False


# global user
USER = 'Mostaq Vai'


# random function
def is_login():
    return LOGGED_IN

def is_created():
    return CREATED


# class based decorator
class Authentication():
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        print('calling...')
        return self.__func()


# decorator
# def is_authenticated(func):
#     def wrapper():
#         func()
#
#     return wrapper


# get method
# @is_authenticated
@Authentication
def get_user_list():
    if is_login():
        print(f"'{USER}' is Authenticated")
    else: print("Not Authenticated!")


# create method
# @is_authenticated
@Authentication
def create_user():
    if is_created():
        print(f"'{USER}' is Created")
    else: print("Not Created!")


"""MAIN"""

# calling method
get_user_list()
create_user()




