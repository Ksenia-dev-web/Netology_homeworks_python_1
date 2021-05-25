# Кто самый умный супергерой?
# Есть API по информации о супергероях.
# Нужно определить кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos.
# Для определения id нужно использовать метод /search/name
#
# Токен, который нужно использовать для доступа к API: 2619421814940190.
# Таким образом, все адреса для доступа к API должны начинаться с https://superheroapi.com/api/2619421814940190/


import requests
import operator

hero_list_data = ['Hulk', 'Captain', 'America', 'Thanos']


def get_data(hero_list):
    result_data = {}
    for hero in hero_list:
        result = requests.get(f'https://www.superheroapi.com/api.php/2619421814940190/search/{hero}')
        result_data[result.json()['results'][0]['name']] = result.json()['results'][0]['powerstats']['intelligence']
    return result_data


def compare_intelligence(dict1):
    sorted_hero_list = sorted(dict1.items(), key=operator.itemgetter(1))
    winner = sorted_hero_list[0][0]
    return winner


result = get_data(hero_list_data)
print(compare_intelligence(result))
