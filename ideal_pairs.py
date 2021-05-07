# Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек (их число может варьироваться):
# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# Выдвигаем гипотезу: лучшие рекомендации мы получим,
# если просто отсортируем имена по алфавиту и познакомим людей с
# одинаковыми индексами после сортировки!
# "Познакомить" пары нам поможет функция zip, а в цикле распакуем zip-объект и выведем информацию в виде:
# Идеальные пары:
# Alex и Emma
# Arthur и Kate
# John и Kira
# Peter и Liza
# Richard и Trisha
# Внимание! Если количество людей в списках будет не совпадать,
# то мы никого знакомить не будет и выведем пользователю предупреждение, что кто-то может остаться без пары!

boys_list = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls_list = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys_list_sort = sorted(boys_list)
girls_list_sort = sorted(girls_list)
pairs_list = zip(boys_list_sort, girls_list_sort)
print('Идеальные пары:', sep='\n')
for elements in pairs_list:
    print(f'{elements[0]} и {elements[1]}')
