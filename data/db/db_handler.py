from collections import defaultdict
import sqlite3


class SQLiteHandler:
    def __init__(self, database_name, timeout=5):
        """Class provide connection and methods to interact
        with sqlite3 database which uses to store notes data
        """
        self.conn = sqlite3.connect(database_name, timeout=timeout)
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
        self.cur.execute("""INSERT INTO notes(id, header)
        VALUES (?, ?);""", (note_widget_id, note_header))
        self.conn.commit()

    def get_one_note(self, note_id: int):
        """ This method provide the ability to get one note data """
        select_query = self.cur.execute("""SELECT id, header
        FROM notes WHERE id = ?;""", (note_id,))
        note_data = select_query.fetchone()
        print(note_data)
        return note_data

    def delete_one_note(self, note_id: int):
        self.cur.execute("""DELETE FROM notes WHERE id = ?;""", (note_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()


if __name__ == "__main__":
    # Tests
    sql_handler = SQLiteHandler("notes_data.db")
    # sql_handler.insert_one_note(1, "pampam")
    sql_handler.get_one_note(1)
    # sql_handler.delete_one_note(1)

