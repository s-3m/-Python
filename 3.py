from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б'
]


def list_union():
    if len(tutors) < len(klasses):
        pair = list(zip(tutors, klasses))
        return pair
    else:
        pair = list(zip_longest(tutors, klasses, fillvalue=None))
        return pair


my_gen = (n for n in list_union())

for i in my_gen:
    print(i)



