from functools import wraps

def val_checker(condition):
    def _val_checker(cal_cube):
        @wraps(cal_cube)
        def wrapper(*args):
            if condition(*args):
                print(cal_cube(*args))
            else:
                msg = 'Wrong value "-5"'
                raise ValueError(msg)
        return wrapper
    return _val_checker




@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

a = calc_cube(10)