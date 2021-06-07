import re


def email_parse(email):
    user_name = re.search(r'(\S+)@', email).group(1)
    domain = re.search(r'@([\w.]+\.[a-z]{2,3})', email).group(1)
    my_dict = {'username': user_name, 'domain': domain}
    print(my_dict)


while True:
    user_answer = input('Введите e-mail: ')
    try:
        email_parse(user_answer)
    except AttributeError:
        msg = f'wrong e-mail: {user_answer}'
        raise ValueError(msg)
    else:
        break
