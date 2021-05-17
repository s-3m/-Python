some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in some_list:
    if i.replace('+', '').isdigit():
        if len(i) == 1:
            some_list[some_list.index(i)] = '"'+'0'+i+'"'
        elif '+' in i or '-' in i:
            some_list[some_list.index(i)] = '"'+i[:1]+'0'+i[1:]+'"'
        else:
            some_list[some_list.index(i)] = '"'+i+'"'


print((' '.join(some_list)).capitalize())
