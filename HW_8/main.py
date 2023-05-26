# Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь 
# также может ввести фамилию, и Вы должны реализовать функционал для изменения и удаления данных

import func

is_active = True

while is_active:
    print("[1] Добавить контакт")
    print("[2] Вывести список контактов")
    print("[3] Редактировать контакт")
    print("[4] Удалить контакт")
    print("[5] Поиск")
    print("[6] Выход")
    print()
    res = int(input("Что желаете? "))

    if res == 1:
        func.add_contact()
    elif res == 2:
        func.show_contact()
    elif res == 3:
        func.edit_contact()
    elif res == 4:
        func.delete_contact()
    elif res == 5:
        func.search()
    elif res == 6:
        is_active = False
    else:
        print("Ошибка")