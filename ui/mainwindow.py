from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from ui.ui_pyside_base.ui_mainwindow import Ui_MainWindow




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
