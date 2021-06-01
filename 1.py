with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    all_str = file.read().split('\n')
    my_gen = (i.split() for i in all_str)
    res = [tuple([h[0], h[5], h[6]]) for h in my_gen ]
    dict_gen = {i[0]: 0 for i in res}

#       ----------------------------- Вычисляем спамера
    for a in res:
        if a[0] in dict_gen:
            dict_gen[a[0]] += 1
    spam_user = dict([max(dict_gen.items(), key=lambda x: x[1])])
    print(spam_user)