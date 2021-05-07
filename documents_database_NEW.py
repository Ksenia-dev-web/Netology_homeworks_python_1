# Я работаю секретарем и мне постоянно приходят различные документы.
# Я должен быть очень внимателен чтобы не потерять ни один документ.
# Каталог документов хранится в следующем виде:
#
#       documents = [
#         {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
#         {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
#         {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
#       ]
# Перечень полок, на которых находятся документы хранится в следующем виде:
#
#       directories = {
#         '1': ['2207 876234', '11-2'],
#         '2': ['10006'],
#         '3': []
#       }
# Задача №1
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
#
# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок,
# спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
# Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций.
# Функции должны иметь выразительное название, передающие её действие.
# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
# Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
# Корректно обработайте кейсы, когда пользователь пытается переместить
# несуществующий документ или переместить документ на несуществующую полку;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.
# Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def finding_person_by_document():
    print('Поиск имени Человека по номеру документа')
    document_number = input('Введите номер документа: ')
    for document in documents:
        if document['number'] == document_number:
            name = document['name']
            print(name)


def finding_shelf_by_document_number(shelf_number = None):
    print('Поиск полки документа')
    document_number = input('Введите номер документа: ')
    for key, value in directories.items():
        if document_number in value:
            shelf_number = key
        if shelf_number is None:
            shelf_number = str("Такого документа нет в базе")
    print(shelf_number)


def list_print():
    print('Список всех документов')
    for item in documents:
        type = item['type']
        number = item['number']
        name = item['name']
        print('{0} "{1}" "{2}"'.format(type, number, name))


def add_document():
    print('Добавление нового документа')
    doc_type = input('Введите тип документа: ')
    number = input('Введите номер документа: ')
    name = input('Введите имя владельца документа: ')
    shelf_number = input('Введите номер полки: ')
    if shelf_number not in directories:
        print("Такой полки не существует")
    new_document = dict(type = doc_type, number = number, name = name)
    documents.append(new_document)
    directories[shelf_number] += [number]
    print("Документ успешно добавлен")


def delete_information():
    print('Удаление документа')
    document_number = input('Введите номер документа: ')
    for document in documents:
        if document['number'] == document_number:
            documents.remove(document)
        for directories_value in directories.values():
            if document_number in directories_value:
                directories_value.remove(document_number)
                print('Документ удален')
    # print(documents)
    # print(directories)


def move_document():
    print('Перемещение документа')
    document_number = input('Введите номер документа для перемещения: ')
    shelf_id = input('Введите целевую полку: ')
    for directories_value in directories.values():
        if document_number in directories_value:
            directories_value.remove(document_number)
    for directories_key in directories.keys():
        if shelf_id in directories_key:
            directories[directories_key].append(document_number)
            print('Документ перемещен')
    # print(directories)


def add_shelf():
    print('Добавление полки')
    shelf_id = input('Номер добавляемой полки: ')
    for directories_key in directories.keys():
        if shelf_id == directories_key:
            print('Такая полка уже есть')
            return
    directories[shelf_id] = []
    print('Полка успешно добавлена')
    # print(directories)


# Путеводитель по командам
functions = {
    'p': finding_person_by_document,
    's': finding_shelf_by_document_number,
    'l': list_print,
    'a': add_document,
    'd': delete_information,
    'm': move_document,
    'as': add_shelf
}

def main():
    print('p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит')
    print('s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится')
    print('l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"')
    print('a – add – команда, которая добавит новый документ в каталог и в перечень полок')
    print('d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок')
    print('m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую')
    print('as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень')
    command = input('Пожалуйста, введите идентификатор команды: ')
    functions[command]()


main()