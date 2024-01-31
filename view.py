# Функции для работы с пользователем

def select_op():
    op=int(input("Выберите пункт меню : \n 1 Добавить контакт \n 2 Поиск контакта \n 3 Удаление контакта \n 4 Изменение контакта \n 5 Показать все записи \n 6 Выход \n "))
    return op
def get_name():
    name = input(" Введите имя ")
    telephone = input( " Введите телефон ")
    string = name + ";" + telephone + "\n"
    return string
def print_info(*args):
    for res in args: 
        if isinstance(res, list):
            counter=1
            for string in res:
                print(f"{counter}){string}")
                counter+=1
        if isinstance(res, str):
            print(res)  
def get_some_info():
    char = input(" Введите строку для поиска ")
    return char        
def select_name():
    num = int(input(" Выберите нужную строку :"))          
    return num - 1