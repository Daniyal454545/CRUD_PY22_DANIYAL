from shop import *

def main():
    print('Что вы хотите сделать? \n 1 - посмореть все продукты \n 2 - создать продукт \n 3 - редактировать продукт \n 4 - удалить продукт \n 5 - взглянуть один продукт')
    user = input('-> ')
    if user == '1':
        print(get_data())
    elif user == '2':
        print(new_product())
    elif user == '3':
        print(reduct_product())
    elif user == '4':
        print(delete_product())
    elif user == '5':
        print(watch_product())
    else:
        print('Error')
main()
while True:
    users = input(' вы хотите продолжить? \n y - yes \n n - no \n ->')
    if users == 'y':
        main()
    else:
        break