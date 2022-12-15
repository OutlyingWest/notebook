import sys
from PySide6.QtWidgets import QApplication

from ui.mainwindow import MainWindow
from ui.note_edit import NoteEditWindow
from ui.note_plate import NotePlateWidget


def main():
    app = QApplication()
    # window_ne = NoteEditWindow()
    # window_np = NotePlateWidget(1)
    main_window = MainWindow()

    # window_ne.show()
    # window_np.show()
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
