import os
import csv
from datetime import datetime
from Note import Note

class NotesModel:
    def __init__(self, data_file="notes.csv"):
        self.data_file = data_file
        self.notes = self.load_data()

    def load_data(self):
        notes = []
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                reader = csv.reader(f, delimiter=";")
                next(reader)
                for row in reader:
                    id, title, content, timestamp = row
                    notes.append(Note(id, title, content, timestamp))
        return notes

    def save_data(self):
        with open(self.data_file, "w", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["ID", "Title", "Content", "Timestamp"])
            for note in self.notes:
                writer.writerow(
                    [note.id, note.title, note.content, note.timestamp])

    def add_note(self, title, content):
        id = len(self.notes) + 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.notes.append(Note(id, title, content, timestamp))
        self.save_data()

    def edit_note(self, id, title, content):
        note = self.get_note_by_id(id)
        if note:
            note.title = title
            note.content = content
            note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.save_data()

    def delete_note(self, id):
        note = self.get_note_by_id(id)
        if note:
            self.notes.remove(note)
            self.save_data()

    def get_notes(self):
        return self.notes

    def get_note_by_id(self, id):
        for note in self.notes:
            if note.id == id:
                return note
        return None
