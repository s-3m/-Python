from random import randint, choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(number, repeat=False):

    """Функция принимает в качестве параметра введенное кол-во шуток и необходимость их повтора.
    Возвращает случайные шутки, собранные из по одному слову их списков."""


    jokes_list = []
    if repeat:
        if number > 5:
            number = 5
        count = 0
        while count < number:
            a = randint(0, len(nouns) - 1)
            b = randint(0, len(adverbs) - 1)
            c = randint(0, len(adjectives) - 1)
            jokes_list.append(f'{nouns.pop(a)} {adverbs.pop(b)} {adjectives.pop(c)}')
            count += 1
    else:
        count = 0
        while count < number:
            jokes_list.append(
                f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
            count += 1
    print(jokes_list)


user_number = int(input('Введие кол-во шуток: '))
need_repeat = input('Повторять ли слова в шутках? (да / нет): ')
repeat = False
if need_repeat == 'нет':
    repeat = True

get_jokes(user_number, repeat)
