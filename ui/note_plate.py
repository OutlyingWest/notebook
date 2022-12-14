from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QWidget
from ui.ui_pyside_base.ui_note_plate import Ui_NotePlate


class NotePlateWidget(QWidget):
    """ Class of note plate in scrolling area in main window """
    write = Signal(int)
    delete = Signal(int)

    def __init__(self, id_widget: int):
        super().__init__()
        # Design init
        self.ui = Ui_NotePlate()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        # Set title to note plate in scrolling area
        self.ui.TitleButton.setText("My title")
        # Connections to buttons on plate
        self.ui.DelButton.clicked.connect(self.press_write_note)
        self.ui.DelButton.clicked.connect(self.press_del)

    @Slot()
    def press_write_note(self):
        """ Open a note edit window """
        pass

    @Slot()
    def press_del(self):
        """ Handle a press on delete button on plate """
        self.delete.emit(self.id_widget)
