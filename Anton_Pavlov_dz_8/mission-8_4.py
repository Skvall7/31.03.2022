def val_checker(func):
    def wrapper(*args):
        if type(args[0]) == int and args[0] > 0:
            x = func(args[0])
        else:
            x = f'Не подходящие значения "{args[0]}"'
        return x
    return wrapper


@val_checker
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))
