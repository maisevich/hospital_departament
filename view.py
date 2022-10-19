import User_interface as ui

def menu_item():
    menu = {
        1: 'Добавить сотрудника',
        2: 'Удалить сотрудника',
        3: 'Редактировать сотрудника',
        4: 'Вывод на экран список сотрудников',
        5: 'Экспортировать файл в формат CSV\n'
    }
    return menu


def print_title():
    print('\nСписок команд \n')


def choose_operation(value):
    if value == 1:
        ui.get_info()
