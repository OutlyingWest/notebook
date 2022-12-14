# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(606, 421)
        MainWindow.setMinimumSize(QSize(500, 300))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.BodyMainGridLayout = QGridLayout()
        self.BodyMainGridLayout.setObjectName(u"BodyMainGridLayout")
        self.ScrollAreaMain = QScrollArea(self.centralwidget)
        self.ScrollAreaMain.setObjectName(u"ScrollAreaMain")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScrollAreaMain.sizePolicy().hasHeightForWidth())
        self.ScrollAreaMain.setSizePolicy(sizePolicy)
        self.ScrollAreaMain.setMinimumSize(QSize(300, 0))
        self.ScrollAreaMain.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(11)
        self.ScrollAreaMain.setFont(font)
        self.ScrollAreaMain.setFrameShape(QFrame.Panel)
        self.ScrollAreaMain.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 378, 339))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.BodyVerticalLayout = QVBoxLayout()
        self.BodyVerticalLayout.setSpacing(0)
        self.BodyVerticalLayout.setObjectName(u"BodyVerticalLayout")
        self.BodyVerticalLayout.setSizeConstraint(QLayout.SetNoConstraint)

        self.verticalLayout_2.addLayout(self.BodyVerticalLayout)

        self.ScrollAreaMain.setWidget(self.scrollAreaWidgetContents)

        self.BodyMainGridLayout.addWidget(self.ScrollAreaMain, 0, 2, 1, 1)

        self.LeftFillerWidget = QWidget(self.centralwidget)
        self.LeftFillerWidget.setObjectName(u"LeftFillerWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(200)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LeftFillerWidget.sizePolicy().hasHeightForWidth())
        self.LeftFillerWidget.setSizePolicy(sizePolicy1)
        self.LeftFillerWidget.setMinimumSize(QSize(200, 100))
        self.LeftFillerWidget.setMaximumSize(QSize(200, 16777215))
        self.LeftFillerWidget.setFont(font)
        self.verticalLayoutWidget = QWidget(self.LeftFillerWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 191, 81))
        self.LeftVerticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.LeftVerticalLayout.setSpacing(6)
        self.LeftVerticalLayout.setObjectName(u"LeftVerticalLayout")
        self.LeftVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.AddButton = QPushButton(self.verticalLayoutWidget)
        self.AddButton.setObjectName(u"AddButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(4)
        sizePolicy2.setHeightForWidth(self.AddButton.sizePolicy().hasHeightForWidth())
        self.AddButton.setSizePolicy(sizePolicy2)

        self.LeftVerticalLayout.addWidget(self.AddButton)

        self.SaveButton = QPushButton(self.verticalLayoutWidget)
        self.SaveButton.setObjectName(u"SaveButton")
        sizePolicy2.setHeightForWidth(self.SaveButton.sizePolicy().hasHeightForWidth())
        self.SaveButton.setSizePolicy(sizePolicy2)

        self.LeftVerticalLayout.addWidget(self.SaveButton)


        self.BodyMainGridLayout.addWidget(self.LeftFillerWidget, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.BodyMainGridLayout, 2, 0, 1, 1)

        self.HeadVerticalLayout = QVBoxLayout()
        self.HeadVerticalLayout.setObjectName(u"HeadVerticalLayout")
        self.MainHeaderLabel = QLabel(self.centralwidget)
        self.MainHeaderLabel.setObjectName(u"MainHeaderLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(150)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.MainHeaderLabel.sizePolicy().hasHeightForWidth())
        self.MainHeaderLabel.setSizePolicy(sizePolicy3)
        self.MainHeaderLabel.setMaximumSize(QSize(16777215, 101))
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(14)
        self.MainHeaderLabel.setFont(font1)
        self.MainHeaderLabel.setAlignment(Qt.AlignCenter)

        self.HeadVerticalLayout.addWidget(self.MainHeaderLabel)


        self.gridLayout_2.addLayout(self.HeadVerticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NoteBook", None))
        self.AddButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.SaveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.MainHeaderLabel.setText(QCoreApplication.translate("MainWindow", u"Notebook", None))
    # retranslateUi

