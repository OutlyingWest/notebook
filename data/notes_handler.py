from dataclasses import dataclass
from data.db.db_handler import SQLiteHandler
from data.notes.notes_file_handler import NoteFileHandler


@dataclass
class DataPaths:
    notes_text_path: str
    db_path: str


def set_paths(notes_text_path: str, db_path: str):
    DataPaths.notes_text_path = notes_text_path
    DataPaths.db_path = db_path


@dataclass
class NotesRestoredData:
    exist_ids: list
    max_note_id: int


def load_notes_data():
    sql_handler = SQLiteHandler('notes_data.db', DataPaths.db_path)
    NotesRestoredData.exist_ids = sql_handler.get_note_ids()
    NotesRestoredData.max_note_id = sql_handler.get_max_note_id()
    sql_handler.close_connection()


class NoteHandler:
    @classmethod
    def save_note(cls, note_id: int, note_text: dict):
        # Write note info to db
        if not note_text:
            note_text = {'title_text': '',
                         'body_text': ''}
        sql_handler = SQLiteHandler('notes_data.db', DataPaths.db_path)
        sql_handler.insert_one_note(note_id, note_text['title_text'])
        sql_handler.close_connection()
        # Write note body text to text file
        file_handler = NoteFileHandler(note_id, note_text['body_text'], DataPaths.notes_text_path)
        file_handler.save_note_to_file()

    @classmethod
    def get_note(cls, note_id):
        sql_handler = SQLiteHandler('notes_data.db', DataPaths.db_path)
        note_header = sql_handler.get_one_note(note_id)
        sql_handler.close_connection()
        file_handler = NoteFileHandler(note_id, file_path=DataPaths.notes_text_path)
        note_body = file_handler.read_note_from_file()
        note_data = {
            'title_text': note_header,
            'body_text': note_body
        }
        return note_data

    @classmethod
    def delete_note(cls, note_id):
        sql_handler = SQLiteHandler('notes_data.db', DataPaths.db_path)
        sql_handler.delete_one_note(note_id)
        sql_handler.close_connection()
        file_handler = NoteFileHandler(note_id, file_path=DataPaths.notes_text_path)
        file_handler.delete_note_file()




