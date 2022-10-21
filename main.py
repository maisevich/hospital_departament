import view
import logger as log

view.print_title()

for k in view.menu_item():
    print(k, view.menu_item()[k])

num_operation = int(input('Введите номер операции: '))

view.choose_operation(num_operation)
