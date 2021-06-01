from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as user:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        user = user.read().split('\n')
        hobby = hobby.read().split('\n')
res_lst = list(zip_longest(user, hobby, fillvalue=None))
with open('users_hobby.txt', 'a', encoding='utf-8') as f:
    for i in res_lst:
        result = f'{i[0]}: {i[1]}\n'
        f.write(result)

