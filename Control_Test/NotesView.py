import datetime


class NotesView:

    def display_notes(self, notes):
        for note in notes:
            print(f"{note.id}: {note.title} - {note.timestamp}")

    def display_note(self, note):
        if note:
            print(
                f"ID: {note.id}\nTitle: {note.title}\nTimestamp: {note.timestamp}\nContent: {note.content}")
        else:
            print("Note not found")
