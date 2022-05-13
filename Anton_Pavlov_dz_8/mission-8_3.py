def type_logger(func):
    def wrapper(*args):
        i = {}
        x = []
        for arg in args:
            i.setdefault(arg, type(arg))
            x += [func(arg)]
        print(i)
        return x

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5, 10, 25)
print(a)
