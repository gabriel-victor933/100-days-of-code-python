import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print('say hello')

@delay_decorator
def say_bye():
    print('say bye')


say_hello()
say_bye()