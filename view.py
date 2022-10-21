import User_interface as ui
import logger as log

def menu_item():
    menu = {
        1: 'Добавить сотрудника',
        2: 'Вывод на экран список сотрудников',
        3: 'Редактировать сотрудника',
        4: 'Удалить сотрудника',
        5: 'Экспортировать файл в формат CSV\n'
    }
    return menu


def print_title():
    print('\nСписок команд \n')


def choose_operation(value):
    if value == 1:
        ui.get_info()
    elif value == 2:
        log.show_list_employees()

