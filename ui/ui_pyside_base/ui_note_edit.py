# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_note_edit.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_NoteEdit(object):
    def setupUi(self, NoteEdit):
        if not NoteEdit.objectName():
            NoteEdit.setObjectName(u"NoteEdit")
        NoteEdit.resize(495, 361)
        font = QFont()
        font.setPointSize(14)
        NoteEdit.setFont(font)
        self.verticalLayout = QVBoxLayout(NoteEdit)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.HeaderNoteLabel = QLabel(NoteEdit)
        self.HeaderNoteLabel.setObjectName(u"HeaderNoteLabel")

        self.verticalLayout.addWidget(self.HeaderNoteLabel)

        self.HeaderNoteLineEdit = QLineEdit(NoteEdit)
        self.HeaderNoteLineEdit.setObjectName(u"HeaderNoteLineEdit")

        self.verticalLayout.addWidget(self.HeaderNoteLineEdit)

        self.BodyNoteLabel = QLabel(NoteEdit)
        self.BodyNoteLabel.setObjectName(u"BodyNoteLabel")

        self.verticalLayout.addWidget(self.BodyNoteLabel)

        self.BodyNoteLineEdit = QTextEdit(NoteEdit)
        self.BodyNoteLineEdit.setObjectName(u"BodyNoteLineEdit")

        self.verticalLayout.addWidget(self.BodyNoteLineEdit)

        self.OkCancelHorizontalLayout = QHBoxLayout()
        self.OkCancelHorizontalLayout.setObjectName(u"OkCancelHorizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.OkCancelHorizontalLayout.addItem(self.horizontalSpacer)

        self.OkButton = QPushButton(NoteEdit)
        self.OkButton.setObjectName(u"OkButton")
        font1 = QFont()
        font1.setPointSize(12)
        self.OkButton.setFont(font1)

        self.OkCancelHorizontalLayout.addWidget(self.OkButton)

        self.CancelButton = QPushButton(NoteEdit)
        self.CancelButton.setObjectName(u"CancelButton")
        self.CancelButton.setFont(font1)

        self.OkCancelHorizontalLayout.addWidget(self.CancelButton)


        self.verticalLayout.addLayout(self.OkCancelHorizontalLayout)


        self.retranslateUi(NoteEdit)

        QMetaObject.connectSlotsByName(NoteEdit)
    # setupUi

    def retranslateUi(self, NoteEdit):
        NoteEdit.setWindowTitle(QCoreApplication.translate("NoteEdit", u"Form", None))
        self.HeaderNoteLabel.setText(QCoreApplication.translate("NoteEdit", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a:", None))
        self.BodyNoteLabel.setText(QCoreApplication.translate("NoteEdit", u"\u0422\u0435\u043a\u0441\u0442 \u0437\u0430\u043c\u0435\u0442\u043a\u0438:", None))
        self.BodyNoteLineEdit.setHtml(QCoreApplication.translate("NoteEdit", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.OkButton.setText(QCoreApplication.translate("NoteEdit", u"Ok", None))
        self.CancelButton.setText(QCoreApplication.translate("NoteEdit", u"Cancel", None))
    # retranslateUi

