from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget
from ui.ui_pyside_base.ui_note_plate import Ui_Form


class NotePlate(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

