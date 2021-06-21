class OnlyDigit(Exception):
    def __init__(self, txt):
        self.txt = txt


dg_lst = []
while True:
    user_answer = input('Для остановки програмы введите "stop". Введите число: ').lower()
    try:
        try_answer = user_answer.replace('-', '')
        try_answer = try_answer.replace('.', '')
        if user_answer != 'stop':
            if try_answer.isdigit():
                dg_lst.append(user_answer)
            else:
                raise OnlyDigit('Это не число. Введите число.')
        else:
            print(dg_lst)
            break
    except OnlyDigit as err:
        print(err)
