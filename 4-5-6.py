from collections import defaultdict


class OutRange(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    desc = 'Самый лучший склад оргтехники!'

    stock = defaultdict(int)
    in_dep = defaultdict(int)

    def on_waterhouse(self, product, quantity):
        self.stock[product] += quantity

    def to_departament(self, product, quantity):
        self.stock[product] -= quantity
        self.in_dep[product] += quantity

    def __str__(self):
        return self.stock[1:]


class OfficeEquipment:
    def __init__(self, full_name, price, ser_num):
        self.price = price
        self.ser_num = ser_num
        self.full_name = full_name


class Printer(OfficeEquipment):
    def __init__(self, full_name, type_pr, price, ser_num):
        super().__init__(full_name, price, ser_num)
        self.type_pr = type_pr


class Scaner(OfficeEquipment):
    def __init__(self, full_name, color, price, ser_num):
        super().__init__(full_name, price, ser_num)
        self.color = color


class Xerox(OfficeEquipment):
    def __init__(self, full_name, size, price, ser_num):
        super().__init__(full_name, price, ser_num)
        self.size = size


a = Printer('Струйный принтер', 'струйный', 200, 'jhf887f9dd')
b = Warehouse()
b.on_waterhouse(a.full_name, 5)
b.on_waterhouse('Лазерный принтер', 10)
b.on_waterhouse('Сканер', 20)
b.on_waterhouse('Ксерокс', 30)
print(b.stock)

while True:
    try:
        user_value = input('Добро пожаловать на склад оргтехники. Выбереите действие и введите соотвествующую цифру:\n'
                           '1 - добавить товар на склад\n'
                           '2 - переместить товар в офис\n'
                           '3 - посмотреть остатки склада\n')

        if int(user_value) == 1:
            try:
                user_value_1_2 = input('1 - Струйный принтер\n2 - лазерный принтер\n3 - Сканер\n4 - Ксерокс\n')
                if int(user_value_1_2) == 1:
                    number = int(input('Введите количество: '))
                    b.on_waterhouse('Струйный принтер', number)
                elif int(user_value_1_2) == 2:
                    number = int(input('Введите количество: '))
                    b.on_waterhouse('Лазерный принтер', number)
                elif int(user_value_1_2) == 3:
                    number = int(input('Введите количество: '))
                    b.on_waterhouse('Сканер', number)
                elif int(user_value_1_2) == 4:
                    number = int(input('Введите количество: '))
                    b.on_waterhouse('Ксерокс', number)
                else:
                    raise OutRange('Позиция отсутствует в представленном списке')
            except OutRange as err:
                print(err)
            except ValueError:
                print('Вы вы ввели не число.')

        elif int(user_value) == 2:
            try:
                user_value_2_2 = input('Какой товар перемещаем?\n'
                                       '1 - Струйный принтер\n'
                                       '2 - лазерный принтер\n'
                                       '3 - Сканер\n'
                                       '4 - Ксерокс\n')
                if int(user_value_2_2) == 1:
                    number = int(input('Введите количество: '))
                    b.to_departament('Струйный принтер', number)
                elif int(user_value_2_2) == 2:
                    number = int(input('Введите количество: '))
                    b.to_departament('Лазерный принтер', number)
                elif int(user_value_2_2) == 3:
                    number = int(input('Введите количество: '))
                    b.to_departament('Сканер', number)
                elif int(user_value_2_2) == 4:
                    number = int(input('Введите количество: '))
                    b.to_departament('Ксерокс', number)
                else:
                    raise OutRange('Позиция отсутствует в представленном списке')
            except OutRange as err:
                print(err)
            except ValueError:
                print('Вы вы ввели не число.')

        elif int(user_value) == 3:
            print(b.stock)
        else:
            raise OutRange('Такой позиции нет в списке')
    except OutRange as err:
        print(err)
    except ValueError:
        print('Вы вы ввели не число.')
