with open('users.csv', 'r', encoding='utf-8') as user:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        user = user.read().replace(',', ' ').split('\n')
        hob_copy = hobby.read()
        hob_lst = hob_copy.split('\n')
        hob_lst.reverse()
        my_dict = {k: None for k in user}
        if len(user) < len(hob_lst):
            exit(1)
        else:
            for key in my_dict:
                if len(hob_lst) != 0:
                    my_dict[key] = hob_lst.pop()
        print(my_dict)


