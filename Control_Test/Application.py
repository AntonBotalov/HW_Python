from ConsoleManager import ConsoleManager
from NotesModel import NotesModel
from NotesPresenter import NotesPresenter
from NotesView import NotesView



class NotesApp:
    def run(self):
        model = NotesModel()
        view = NotesView()
        presenter = NotesPresenter(model, view)
        clear = ConsoleManager().clear_console
        

        while True:
            clear()
            print("Меню:")
            print("1. Добавить заметку")
            print("2. Редактировать заметку")
            print("3. Удалить заметку")
            print("4. Показать все заметки")
            print("5. Показать содержимое заметки")
            print("6. Выход")

            choice = input("Введите команду: ")

            if choice == "1":
                clear()
                title = input("Введите заголовок: ")
                content = input("Введите контент: ")
                presenter.add_note(title, content)
                input("Заметка создана\nДля продолжения нажмите Enter")
            elif choice == "2":
                clear()
                id = int(input("Введите ID заметки: "))
                title = input("Введите заголовок: ")
                content = input("Введите контент: ")
                presenter.edit_note(id, title, content)
                input("Заметка изменена\nДля продолжения нажмите Enter")
            elif choice == "3":
                clear()
                id = int(input("Введите ID заметки: "))
                presenter.delete_note(id)
                input("Заметка удалена\nДля продолжения нажмите Enter")
            elif choice == "4":
                clear()
                presenter.display_notes()
                input("Для продолжения нажмите любую клавишу Enter")
            elif choice == "5":
                clear()
                id = int(input("Enter ID: "))
                presenter.display_note(id)
                input("Для продолжения нажмите Enter")
            elif choice == "6":
                print("Пока)")
                break
            else:
                print("Команда не найдена")
