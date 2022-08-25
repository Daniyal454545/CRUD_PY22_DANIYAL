import json


FILE = 'db.json'


# сериализируем json в python
def get_data():
    with open(FILE) as file:
        return json.load(file)


# даем id для продукта
def new_id():
    with open('id.txt', 'r') as file:
        id = int(file.read())
        id += 1
    with open('id.txt', 'w') as file:
        file.write(str(id))
    return id


# Создаем продукт
def new_product():
    print('Создаем продукт🤓')
    data = get_data()
    product = {
        'id': new_id(),
        'mark': input('Введите марку продукта для создания продукта -> '),
        'model': input('Введите модель продукта -> '),
        'year': int(input('Введите год выпуска -> ')),
        'color': input('Введите цвет продукта -> '),
        'power': input('Введите обьем -> '),
        'transmission': input('Коробка -> '),
        'price': int(input('Цена продукта -> '))
    }
    data.append(product)
    with open(FILE, 'w') as file:
        json.dump(data, file)
    return 'Продукт создан'



# редактируем продукт


def reduct_product():
    print('Редактирования продукта 😜')
    data = get_data()
    # flag = False
    id = int(input('Введите id продукта для изменении -> '))
    product = list(filter(lambda x: x['id'] == id, data))
    if not product:
        return 'вы не правильно ввели id продукта'
    index_ = data.index(product[0])
    user = input('Что вы хотите изменить? p.s введите ниже указанные цифры 🤫 \n 1 - Марку \n 2 - Модель \n 3 - Год \n 4 - Цвет \n 5 - Обьем \n 6 - Коробка \n 7 - Цена \n ->')
    if user == '1':
        data[index_]['mark'] = input('Введите новую марку -> ')
    elif user == '2':
        data[index_]['model'] = input('Введите новую модель -> ')
    elif user == '3':
        data[index_]['year'] = input('Введите год машины -> ')
    elif user == '4':
        data[index_]['color'] = input('Какого цвета машина  -> ')
    elif user == '5':
        data[index_]['power'] = input('Введите обьем машины -> ')
    elif user == '6':
        data[index_]['transmission'] = input('Коробка  -> ')
    elif user == '7':
        data[index_]['price'] = input('Введите цену -> ')
    else:
        return 'Такой команды нету 🫤'

    with open(FILE, 'w') as file:
        json.dump(data, file)
    return 'ваш продукт успешно изменен 🥳'

def delete_product():
    data = get_data()
    id = int(input('Введите id для удалении -> '))
    product = list(filter(lambda x:x['id'] == id, data))
    if not product:
        return 'Такого продукта нету 😤'
    index_ = data.index(product[0])
    data.pop(index_)
    json.dump(data, open(FILE, 'w'))
    return 'Продукт удален!'

def watch_product():
    data = get_data()
    id = int(input('Введите id продукта'))
    product = list(filter(lambda x:x['id'] == id, data))
    
    if product:
        return product[0]
    else:
        return 'Такого продукта нету!'