# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_note_plate.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_NotePlate(object):
    def setupUi(self, NotePlate):
        if not NotePlate.objectName():
            NotePlate.setObjectName(u"NotePlate")
        NotePlate.resize(479, 40)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(NotePlate.sizePolicy().hasHeightForWidth())
        NotePlate.setSizePolicy(sizePolicy)
        NotePlate.setMinimumSize(QSize(200, 0))
        NotePlate.setMaximumSize(QSize(16777215, 40))
        NotePlate.setBaseSize(QSize(0, 40))
        NotePlate.setWindowOpacity(1.000000000000000)
        self.horizontalLayout = QHBoxLayout(NotePlate)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleButton = QPushButton(NotePlate)
        self.TitleButton.setObjectName(u"TitleButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TitleButton.sizePolicy().hasHeightForWidth())
        self.TitleButton.setSizePolicy(sizePolicy1)
        self.TitleButton.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.TitleButton.setFont(font)

        self.horizontalLayout.addWidget(self.TitleButton)

        self.DelButton = QPushButton(NotePlate)
        self.DelButton.setObjectName(u"DelButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(40)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.DelButton.sizePolicy().hasHeightForWidth())
        self.DelButton.setSizePolicy(sizePolicy2)
        self.DelButton.setMaximumSize(QSize(40, 40))
        font1 = QFont()
        font1.setFamilies([u"Segoe Print"])
        font1.setPointSize(18)
        self.DelButton.setFont(font1)
        self.DelButton.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout.addWidget(self.DelButton)


        self.retranslateUi(NotePlate)

        QMetaObject.connectSlotsByName(NotePlate)
    # setupUi

    def retranslateUi(self, NotePlate):
        NotePlate.setWindowTitle(QCoreApplication.translate("NotePlate", u"Form", None))
        self.TitleButton.setText(QCoreApplication.translate("NotePlate", u"Title", None))
        self.DelButton.setText(QCoreApplication.translate("NotePlate", u"X", None))
    # retranslateUi

