path = 'phone_namber.txt'

def add_contact():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    second_name = input("Введите отчество: ")
    phone = input("Введите телефон: ")
    with open(path, 'a+', encoding='utf-8') as data:
        data.write(f"{surname}, {name}, {second_name}, {phone}\n")
    print("Контакт создан")

def show_contact():
    with open(path, 'r', encoding='utf-8') as data:
        i=1
        for line in data:
            print(f"{i}. {line}")
            i+=1

def search():
    with open(path, 'r', encoding='utf-8') as data:
        word  = input("Введите, что ищете: ")
        index = 0
        count = 0
        for line in data:
            if word in line:
                print(line)
                count+=1
                index+=1
        if count == 0:
            print('Такого человека нет')
        else:
            print('[1] - удалить\n[2] - редактировать\nДля выхода нажми любую клавишу')
            res = input()
            if res == '1': fast_delate(index)
            if res == '2': fast_edit(index)
            else: print()

def delete_contact():
    contacts = list()
    with open(path, 'r', encoding="utf-8") as f:
        contacts = list(map(lambda x: x.strip(), f.readlines()))
        index = int(input("Введите номер строчки для удаления: ")) - 1
        del contacts[index]

    rewrite(contacts)

def fast_delate(index):
    contacts = list()
    with open(path, 'r', encoding="utf-8") as f:
        contacts = list(map(lambda x: x.strip(), f.readlines()))
        del contacts[index]

    rewrite(contacts)

def edit_contact():
    contacts = list()
    with open(path, 'r', encoding="utf-8") as f:
        contacts = list(map(lambda x: x.strip(), f.readlines()))
        index = int(input("Введите номер строчки для редактирования:: ")) - 1
        surname = input("Фамилия: ")
        name = input("Имя: ")
        second_name = input("Отчество: ")
        phone = input("Телефон: ")
        contacts[index] = f"{surname},{name},{second_name},{phone}"
    
    rewrite(contacts)

def fast_edit(index):
  contacts = list()
  with open(path, 'r', encoding="utf-8") as f:
    contacts = list(map(lambda x: x.strip(), f.readlines()))
    surname = input("Фамилия: ")
    name = input("Имя: ")
    second_name = input("Отчество: ")
    phone = input("Телефон: ")
    contacts[index] = f"{surname},{name},{second_name},{phone}"
    rewrite(contacts)
  

def rewrite(contacts):
    with open(path, 'w', encoding="utf-8") as f:
        for i in contacts:
            f.write(f"{i}\n")