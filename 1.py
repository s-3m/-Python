class Date:
    def __init__(self, date):
        self.date = date

    def xxx(self):
        return self.date

    @classmethod
    def int(cls, obj):
        try:
            int_str = [int(i) for i in cls.xxx(obj).split('-')]
            if len(int_str) != 3:
                raise ValueError
            else:
                return int_str
        except ValueError:
            return f'Введенные данные не являются числом или нарушен формат ввода!'

    @staticmethod
    def valid(obj):
        try:
            date_list = Date.int(obj)
            if date_list[0] < 1 or date_list[0] > 31:
                return f'Число находится вне предела'
            elif date_list[1] < 1 or date_list[1] > 12:
                return f'Месяц находится вне предела'
            elif date_list[2] < 1 or date_list[2] > 2999:
                return f'Год находится вне предела'
            else:
                return f'Все данные корректны'
        except TypeError as err:
            return err


user_answer = input('Введите дату в формате дд-мм-гггг: ')
z = Date(user_answer)
print(Date.int(z))
print(Date.valid(z))
