def my_decorator(func):
    def wrapper():
        print("f(x) = x**2 + 2")
        print(func)
    return wrapper


def licz(x):
    return x**2 + 2


decorated = my_decorator(licz(3))
decorated()
