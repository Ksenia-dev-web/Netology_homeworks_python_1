# Необходимо написать программу для кулинарной книги.
#
# Список рецептов должен храниться в отдельном файле в следующем формате:
#
# Название блюда
# Количество ингредиентов в блюде
# Название ингредиента | Количество | Единица измерения
# Название ингредиента | Количество | Единица измерения
# ...

from pprint import pprint

cook_book = {}
with open('text.txt', encoding='utf-8') as file:
    for line in file:
        dish_name = line.strip()
        # print(dish_name)
        ingredient_count = int(file.readline())
        recipe = []
        # print(ingredient_count)
        for i in range(ingredient_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            recipe_dict = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
            recipe.append(recipe_dict)
            cook_book[dish_name] = recipe
        file.readline()
pprint(cook_book)

# Нужно написать функцию, которая на вход принимает список блюд
# из cook_book и количество персон для кого мы будем готовить
# На выходе мы должны получить словарь с названием ингредиентов и
# его количества для блюда. Например, для такого вызова
#
# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# Должен быть следующий результат:
#
# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }


def get_shop_list_by_dishes(dishes, person_count):
    temp = {}
    shopping_dict = {}
    for dish_id in dishes_list:
        if dish_id.capitalize() in cook_book.keys():
            for key, value in cook_book.items():
                temp = cook_book[dish_id.capitalize()]
                for i in temp:
                    shopping_dict[i['ingredient_name']] = {'measure': i['measure'], 'quantity': int(i['quantity']) * person_count}
        else:
            print('Ошибка')
    return shopping_dict


dishes = input('Блюда, которые будем готовить: ')
dishes_list = dishes.split(', ')
person_count = int(input('Количество гостей: '))
pprint(get_shop_list_by_dishes(dishes_list, person_count))
