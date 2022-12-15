from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QMainWindow

from ui.note_plate import NotePlateWidget

from ui.ui_pyside_base.ui_mainwindow import Ui_MainWindow


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
        pass

