from itertools import zip_longest


with open('users.csv', 'r', encoding='utf-8') as user:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:

        res_lst = zip_longest((' '.join(i.split(',')) for i in user), hobby, fillvalue=None)

        with open('users_hobby.txt', 'a', encoding='utf-8') as f:
            for i in res_lst:
                print(f'{str(i[0]).strip()}: {str(i[1]).strip()}', file=f)
