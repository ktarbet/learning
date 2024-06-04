
def multiply(a, b):
    return a * b


def calculate(f, n1, n2):
    return f(n1, n2)


# functions are objects
x = calculate(multiply, 2, 2)
print(x)


def outer_f():
    print("outer..")

    def inner_f():
        print("inner")

    return inner_f

f = outer_f()
f()