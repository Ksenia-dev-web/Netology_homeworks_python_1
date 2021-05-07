# Выведите на экран все уникальные гео-ID
# из значений словаря ids.
# Т. е. список вида [213, 15, 54, 119, 98, 35]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user8': [25654, 8562354, 2119, 119, 119],
       'user3': [213, 98, 98, 35]}


sum_ids_list = []

for key, value in ids.items():
     sum_ids_list += value

# print(sum_ids_list)
unique = set(sum_ids_list)
result = list(unique)

print(result)

