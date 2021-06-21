class MyExeption(Exception):
    def __init__(self, txt):
        self.txt = txt


num_one = input('Введите делимое: ')
try:
    a = int(num_one)
except ValueError:
    print('Вы ввели не число')
else:
    num_two = input('Введите делитель: ')
    try:
        b = int(num_two)
        if b == 0:
            raise MyExeption('На ноль делить нельзя!')
    except MyExeption as err:
        print(err)
    except ValueError:
        print('Вы ввели не число')
    else:
        print(int(num_one) / int(num_two))
