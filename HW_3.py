user_answer = int(input('Введите количество процентов от 1 до 20: '))

if user_answer >= 5 or user_answer == 0:
    print(f'Вы ввели {user_answer} процентов')
elif user_answer == 1:
    print(f'Вы ввели {user_answer} процент')
else: print(f'Вы ввели {user_answer} процента')