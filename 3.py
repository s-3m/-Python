from functools import wraps


def type_logger(calc_cube):
    @wraps(calc_cube)
    def wrapper(*args):
        for i in args:
            print(f'{calc_cube.__name__} ({i}: {type(i)})', end=', ')
    return wrapper


@type_logger
def calc_cube(x):
    print(x ** 3)

print(calc_cube)
a = calc_cube(5)
