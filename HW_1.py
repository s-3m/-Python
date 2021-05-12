
def time_info(user_duration):
    user_duration = int(user_duration)
    if user_duration < 60:
        print(f'{user_duration} сек')
    elif 3599 >= user_duration > 59:
        print(f'{user_duration // 60} мин {user_duration % 60} сек')
    elif 86400 > user_duration > 3599:
        hours = user_duration // 3600
        minutes = (user_duration % 3600) // 60
        seconds = int(user_duration - (hours * 3600 + minutes * 60))
        print(f'{hours} час {minutes} мин {seconds} сек')
    else:
        days = user_duration // 86400
        user_duration_remains = user_duration % 86400
        hours = user_duration_remains // 3600
        user_duration_remains = user_duration_remains % 3600
        minutes = user_duration_remains // 60
        seconds = user_duration_remains % 60
        print(f'{days} дн {hours} час {minutes} мин {seconds} сек')


while True:
    print('Для выхода введите "стоп"')
    duration = input('Введите продолжительность промежутка времени: ')
    if duration == 'стоп':
        break
    else:
        time_info(duration)
