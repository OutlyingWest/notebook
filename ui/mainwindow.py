from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QMainWindow

from ui.note_plate import NotePlateWidget
from ui.note_edit import NoteEditWindow

from ui.ui_pyside_base.ui_mainwindow import Ui_MainWindow
from data.notes_handler import NoteHandler, NotesRestoredData


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Design init
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.BodyVerticalLayout.setAlignment(Qt.AlignTop)
        # Counter of note_plate_widgets ids
        self.counter_id: int = 0
        # Dict of all note_plate_widgets
        self.note_plate_widgets = {}
        # Restore notes from ROM
        self.__restore_notes()
        # Connections to buttons on left field of main window
        self.ui.AddButton.clicked.connect(self.add_note_plate_widget)
        self.ui.SaveButton.clicked.connect(self.save_notes)

    @Slot()
    def add_note_plate_widget(self):
        self.counter_id += 1
        # Creation of instance of NotePlateWidget object
        note_plate_widget = NotePlateWidget(self.counter_id)
        # Addition of a new NotePlateWidget object to dictionary
        self.note_plate_widgets[self.counter_id] = note_plate_widget
        # Addition of a new NotePlateWidget object to main window
        self.ui.BodyVerticalLayout.addWidget(note_plate_widget)
        note_plate_widget.delete.connect(self.delete_note_plate_widget)

    @Slot(int)
    def delete_note_plate_widget(self, npw_id: int):
        # Deletion note_plate_widget from note_plate_widgets dict
        if not self.note_plate_widgets.pop(npw_id, None):
            print(f'note_plate_widget with id: {npw_id} does not exist')
        note_plate_widget = self.sender()
        self.ui.BodyVerticalLayout.removeWidget(note_plate_widget)

        note_plate_widget.deleteLater()

    @Slot()
    def save_notes(self):
        """ Save all added notes"""
        for note_id, note_plate_widget in self.note_plate_widgets.items():
            note_text = note_plate_widget.note_text
            NoteHandler.save_note(note_id=note_id,
                                  note_text=note_text)

    def __restore_notes(self):
        restored_notes_ids = NotesRestoredData.exist_ids
        restored_max_id = NotesRestoredData.max_note_id
        for note_id in restored_notes_ids:
            restored_note_data = NoteHandler.get_note(note_id)
            # Creation of a restored instance of NotePlateWidget object
            note_plate_widget = NotePlateWidget(note_id)
            note_plate_widget.update_note(note_text=restored_note_data)
            # Creation of a restored instance of NoteEditWindow object
            note_plate_widget.note_edit_window = NoteEditWindow()
            note_plate_widget.note_edit_window.ui.HeaderNoteLineEdit.setText(restored_note_data['title_text'])
            note_plate_widget.note_edit_window.ui.BodyNoteLineEdit.setText(restored_note_data['body_text'])
            note_plate_widget.note_edit_window.note_text = restored_note_data
            # Addition of a restored NotePlateWidget object to dictionary
            self.note_plate_widgets[note_id] = note_plate_widget
            # Addition of a restored NotePlateWidget object to main window
            self.ui.BodyVerticalLayout.addWidget(note_plate_widget)
            note_plate_widget.delete.connect(self.delete_note_plate_widget)
            # Restore counter
            if restored_max_id:
                self.counter_id = restored_max_id






