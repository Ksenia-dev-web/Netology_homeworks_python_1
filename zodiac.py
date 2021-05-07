# Разработать приложение для определения знака зодиака по дате рождения.
# Пример:
# 
# Введите месяц: март
# Введите число: 6
# 
# Вывод:
# Рыбы

month = input('Введите месяц: ')
day = int(input('Введите число: '))

if month == 'Январь'.casefold():
    if 1 <= day < 20:
        print('Козерог')
    elif 20 <= day <= 31:
        print('Водолей')
elif month == 'Февраль'.casefold():
    if 1 <= day < 19:
        print('Водолей')
    elif 19 <= day <= 29:
        print('Рыбы')
elif month == 'Март'.casefold():
    if 1 <= day < 21:
        print('Рыбы')
    elif 21 <= day <= 31:
        print('Овен')
elif month == 'Апрель'.casefold():
    if 1 <= day < 21:
        print('Овен')
    elif 21 <= day <= 30:
        print('Телец')
elif month == 'Май'.casefold():
    if 1 <= day < 21:
        print('Телец')
    elif 21 <= day <= 31:
        print('Близнецы')
elif month == 'Июнь'.casefold():
    if 1 <= day < 21:
        print('Близнецы')
    elif 21 <= day <= 30:
        print('Рак')
elif month == 'Июль'.casefold():
    if 1 <= day < 23:
        print('Рак')
    elif 23 <= day <= 31:
        print('Лев')
elif month == 'Август'.casefold():
    if 1 <= day < 23:
        print('Лев')
    elif 23 <= day <= 31:
        print('Дева')
elif month == 'Сентябрь'.casefold():
    if 1 <= day < 24:
        print('Дева')
    elif 24 <= day <= 30:
        print('Весы')
elif month == 'Октябрь'.casefold():
    if 1 <= day < 24:
        print('Весы')
    elif 24 <= day <= 31:
        print('Скорпион')
elif month == 'Ноябрь'.casefold():
    if 1 <= day < 22:
        print('Скорпион')
    elif 22 <= day <= 30:
        print('Стрелец')
elif month == 'Декабрь'.casefold():
    if 1 <= day < 22:
        print('Стрелец')
    elif 22 <= day <= 31:
        print('Козерог')
else:
    print('Ошибка')
