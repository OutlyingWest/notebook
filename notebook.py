import os
import sys
from PySide6.QtWidgets import QApplication

from ui.mainwindow import MainWindow
from ui.note_edit import NoteEditWindow
from ui.note_plate import NotePlateWidget

from data.notes_handler import set_paths, load_notes_data


def main():
    load_config()
    app = QApplication()
    # window_ne = NoteEditWindow()
    # window_np = NotePlateWidget(1)
    main_window = MainWindow()

    # window_ne.show()
    # window_np.show()
    main_window.show()
    sys.exit(app.exec())


def load_config():
    project_path = os.path.dirname((os.path.abspath(__file__)))
    set_paths(notes_text_path=project_path + r'/data/notes/',
              db_path=project_path + r'/data/db/')
    load_notes_data()


if __name__ == "__main__":
    main()
