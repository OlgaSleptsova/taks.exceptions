documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "passport", "number": "10008"}]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def key_name(dicts):
    for doc in dicts:
        try:
            doc['name'] in doc
        except KeyError:
            print('Нет ключа с таким названием!')
        else:
            print(doc['name'])

key_name(documents)