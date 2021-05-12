def sum_total(user_list, value=0):
    sum_total = 0
    for i in user_list:
        i += value
        number = i
        sum_number = 0
        while number != 0:
            sum_number = sum_number + number % 10
            number = number // 10
        if sum_number % 7 == 0:
            sum_total += i
    return sum_total

user_list = [i ** 3 for i in range(1000) if i % 2 != 0]

print(sum_total(user_list))
print(sum_total(user_list, 17))
