from PySide6.QtWidgets import QWidget
from ui.ui_pyside_base.ui_note_edit import Ui_NoteEdit


class NoteEditWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NoteEdit()
        self.ui.setupUi(self)
