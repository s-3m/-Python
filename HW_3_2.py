def thesaurus(*args):
    name_dict = {}
    for name in args:
        name_dict[name[0]] = []
    for name in args:
        name_dict[name[0]].append(name)
    sort_touple = sorted(name_dict.items(), key=lambda i: i[0])      #сортировка по ключу
    print(dict(sort_touple))


thesaurus("Марина", "Иван", "Мария", "Петр", "Илья", "Роман", "Павел", "Матвей", "Ренат")
