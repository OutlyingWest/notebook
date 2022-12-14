from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QMainWindow

from ui.note_plate import NotePlateWidget

from ui.ui_pyside_base.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.BodyVerticalLayout.setAlignment(Qt.AlignTop)
        self.counter_id: int = 0
        self.ui.AddButton.clicked.connect(self.add_note_plate_widget)

    @Slot()
    def add_note_plate_widget(self):
        self.counter_id += 1
        note_plate_widget = NotePlateWidget(self.counter_id)
        self.ui.BodyVerticalLayout.addWidget(note_plate_widget)
        note_plate_widget.delete.connect(self.delete_note_plate_widget)

    @Slot(int)
    def delete_note_plate_widget(self, wid: int):
        widget = self.sender()
        self.ui.BodyVerticalLayout.removeWidget(widget)
        widget.deleteLater()
