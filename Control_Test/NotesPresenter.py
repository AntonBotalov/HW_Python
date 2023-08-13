import NotesModel

class NotesPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_note(self, title, content):
        self.model.add_note(title, content)

    def edit_note(self, id, title, content):
        self.model.edit_note(id, title, content)

    def delete_note(self, id):
        self.model.delete_note(id)

    def display_notes(self):
        notes = self.model.get_notes()
        self.view.display_notes(notes)

    def display_note(self, id):
        note = self.model.get_note_by_id(id)
        self.view.display_note(note)
