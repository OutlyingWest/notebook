from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QWidget
from ui.ui_pyside_base.ui_note_plate import Ui_NotePlate
from ui.note_edit import NoteEditWindow


class NotePlateWidget(QWidget):
    """ Class of note plate in scrolling area in main window """
    delete = Signal(int)

    def __init__(self, id_widget: int):
        super().__init__()
        # Design init
        self.ui = Ui_NotePlate()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        # Set default title to note plate in scrolling area
        self.ui.TitleButton.setText("New Note")
        # Object of note edit modal window
        self.note_edit_window = None
        # Note text dict
        self.note_text = {}
        # Connections to buttons on plate
        self.ui.TitleButton.clicked.connect(self.press_write_note)
        self.ui.DelButton.clicked.connect(self.press_del)

    @Slot()
    def press_write_note(self):
        """ Open a note edit window """
        note_edit_widget = self.sender()
        if not self.note_edit_window:
            self.note_edit_window = NoteEditWindow()
            # Get empty note text dictionary
            self.note_text = self.note_edit_window.note_text
            # Create signal connection
            self.note_edit_window.ok_signal.connect(self.update_note)
            # Show edit window
            self.note_edit_window.show()
        elif self.note_edit_window.is_canceled:
            # Get empty note text dictionary
            self.note_text = self.note_edit_window.note_text
            # Show edit window
            self.note_edit_window.show()

        else:
            self.note_edit_window.show()

    @Slot()
    def press_del(self):
        """ Handle a press on delete button on plate """
        self.delete.emit(self.id_widget)

    @Slot(dict)
    def update_note(self, note_text: dict):
        new_title = note_text['title_text']
        if new_title:
            self.ui.TitleButton.setText(new_title)

        self.note_text = note_text

