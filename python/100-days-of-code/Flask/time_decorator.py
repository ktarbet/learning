import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


def speed_calc_decorator(f):
    def time_me():
        t1 = time.time()
        f()
        t2 = time.time()
        seconds = t2 - t1
        print(f"{seconds}s for  {f.__name__}")
    return time_me


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        x = i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()
