#                                                       5 задание
#                                                         Часть 1

#   Первую часть 5 ДЗ сделал в двух вариантах, сначала, как написано в условиях ДЗ - числа вида 34.3 преобразуются в 34 руб 03 коп.
#   Но, фактически, это неправильно, ведь 34 руб 03 коп - это 34.03, а 34.3 - это 34 руб. 30 коп.
#   Поэтому сделал подчасть 2 к этому заданию, с корректным отображением.

#           Подчасть 1

prices = [57.8, 46.51, 97, 98.08, 10.53, 87, 33.3, 0.25, 55.66, 81.22]
format_prices = []
for i in prices:
    i = str(i)
    if '.' in i:
        a = i.split('.')
        format_prices.append(f'{a[0]} руб. {int(a[1]):02} коп.')
    else:
        format_prices.append(f'{i} руб. 00 коп.')
print(', '.join(format_prices))


#              Подчасть 2

format_prices = []
for i in prices:
    i = str(i)
    if '.' in i:
        a = i.split('.')
        if len(a[1]) > 1:
            format_prices.append(f'{a[0]} руб. {a[1]} коп.')
        else:
            format_prices.append(f'{a[0]} руб. {int(a[1]) * 10} коп.')
    else:
        format_prices.append(f'{i} руб. 00 коп.')
print(', '.join(format_prices))

#                                                         Часть 2

print('ID до сортировки:', id(prices))
prices.sort()
print(prices)
print('ID после сортировки:', id(prices))        # id до и после сортировки одинаковы

#                                                         Часть 3


new_list = sorted(prices, reverse=True)
print(new_list)


#                                                         Часть 4
# Не стал заморачиваться, чтобы сделать красиво (например, 1 место - ..., 2 место - ...), т.к. в условии задания не было сказано.


for i in new_list[:5]:
    print('Пять самых дорогих товаров:')
    print(i)

