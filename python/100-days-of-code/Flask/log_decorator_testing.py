inputs = [1, 2, 4]


def log_decorator(f):
    def wrapper(*args, **kwargs):
        print(f"method: {f.__name__}({args})")
        #rval = f(args[0], args[1], args[2])
        rval = f(*args)
        print(f"result ={rval}")
    return wrapper


@log_decorator
def a_function(a, b, c):
    return a * b * c


a_function(inputs[0], inputs[1], inputs[2])

