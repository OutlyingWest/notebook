import sqlite3


class SQLiteHandler:
    def __init__(self, database_name, db_path: str, timeout=5):
        """Class provide connection and methods to interact
        with sqlite3 database which uses to store notes data
        """
        self.conn = sqlite3.connect(db_path + database_name, timeout=timeout)
        self.cur = self.conn.cursor()
        self.conn.commit()
        self.__create_table()

    def __create_table(self):
        """ Protected method to creation notes data table in db """
        self.cur.execute("""CREATE TABLE IF NOT EXISTS notes(
            id INT NOT NULL PRIMARY KEY,
            header STR NOT NULL);""")
        self.conn.commit()

    def insert_one_note(self, note_widget_id: int, note_header: str):
        """This method provide the ability to insert one line of data
        to notes table
        """
        # Check of existence note with current note_widget_id
        select_query = self.cur.execute("""SELECT id
        FROM notes WHERE id = ?;""", (note_widget_id,))
        note_data = select_query.fetchone()
        if not note_data:
            self.cur.execute("""INSERT INTO notes(id, header)
            VALUES (?, ?);""", (note_widget_id, note_header))
            self.conn.commit()
        else:
            self.cur.execute("""
            UPDATE notes
            SET header = ? 
            WHERE id = ?""", (note_header, note_widget_id))
            self.conn.commit()

    def get_one_note(self, note_id: int) -> tuple:
        """ This method provide the ability to get one note data """
        select_query = self.cur.execute("""SELECT header
        FROM notes WHERE id = ?;""", (note_id,))
        note_header = select_query.fetchone()[0]
        # print(note_header)
        return note_header

    def delete_one_note(self, note_id: int):
        self.cur.execute("""DELETE FROM notes WHERE id = ?;""", (note_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

    def get_max_note_id(self):
        select_query = self.cur.execute("""SELECT MAX(id) FROM notes""")
        note_max_id = select_query.fetchone()[0]
        return note_max_id

    def get_note_ids(self):
        select_query = self.cur.execute("""SELECT id FROM notes""")
        note_ids = select_query.fetchall()
        note_ids = [note_id[0] for note_id in note_ids]
        return note_ids


if __name__ == "__main__":
    # Tests
    sql_handler = SQLiteHandler("notes_data.db", r'C:\Users\px\PycharmProjects\Tests\\')
    sql_handler.insert_one_note(1, "pam")
    sql_handler.insert_one_note(2, "psdfm")
    sql_handler.insert_one_note(3, "psdfmsdf")
    sql_handler.get_one_note(3)
    # sql_handler.delete_one_note(1)
    # sql_handler.get_max_note_id()
    # sql_handler.get_note_ids()

