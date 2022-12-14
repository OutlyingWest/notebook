import os
import sys
from PySide6.QtWidgets import QApplication

from ui.mainwindow import MainWindow
from data.notes_handler import set_paths, load_notes_data


def main():
    load_config()
    app = QApplication()
    main_window = MainWindow()

    main_window.show()
    sys.exit(app.exec())


def load_config():
    project_path = os.path.dirname((os.path.abspath(__file__)))
    set_paths(notes_text_path=project_path + r'/data/notes/',
              db_path=project_path + r'/data/db/')
    load_notes_data()


if __name__ == "__main__":
    main()
