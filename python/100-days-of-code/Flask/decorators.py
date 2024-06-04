import time

def delay_decorator(function):
    def wrapper_f():
        #before
        time.sleep(2)
        function()
        # after
    return wrapper_f


@delay_decorator
def hello():
    print("Hello")

def bye():
    print("bye")

@delay_decorator
def greet():
    print("how are you?")

d = delay_decorator(hello)
d()
hello()
