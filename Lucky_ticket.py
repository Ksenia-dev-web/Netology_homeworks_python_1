# Проверить, счастливый ли билет
number = 545455

num_1 = number // 100000
num_2 = number // 10000 % 10
num_3 = number // 1000 % 10
num_4 = number // 100 % 10
num_5 = number // 10 % 10
num_6 = number % 10
sum_1 = num_1 + num_2 + num_3
sum_2 = num_4 + num_5 + num_6
if sum_1 == sum_2:
    print('Lucky you!')
else:
    print('May be next time?')
