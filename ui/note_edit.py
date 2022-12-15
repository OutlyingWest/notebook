from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QWidget, QDialog
from ui.ui_pyside_base.ui_note_edit import Ui_NoteEdit


class NoteEditWindow(QWidget):
    ok_signal = Signal(dict)

    def __init__(self):
        super().__init__()
        self.ui = Ui_NoteEdit()
        self.ui.setupUi(self)
        self.is_canceled = False
        self.note_text = {
            'title_text': '',
            'body_text': ''}
        self.ui.OkButton.clicked.connect(self.press_ok)
        self.ui.CancelButton.clicked.connect(self.press_cancel)

    @Slot()
    def press_ok(self):
        title_text = self.ui.HeaderNoteLineEdit.text()
        body_text = self.ui.BodyNoteLineEdit.toPlainText()
        self.note_text = {
            'title_text': title_text,
            'body_text': body_text}
        self.ok_signal.emit(self.note_text)
        self.hide()

    @Slot()
    def press_cancel(self):
        # Indication to note plate that note edit object was deleted
        self.is_canceled = True
        self.ui.HeaderNoteLineEdit.setText(self.note_text['title_text'])
        self.ui.BodyNoteLineEdit.setText(self.note_text['body_text'])
        # Close window
        self.hide()




