date_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

print(date_list)
for i in date_list:
    print(f"Привет, {i[i.rfind(' '):].title()}!")