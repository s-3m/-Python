num_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
            'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
            'nine': 'девять', 'ten': 'десять'}


def num_translate(number):
    if number.istitle():
        print(num_dict.get(number.lower()).title())
    else:
        print(num_dict.get(number))

user_value = input('Введите числительное от 0 до 10, которое нужно перевести: ')
num_translate(user_value)
