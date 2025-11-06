# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import recursos_rc

class Ui_PlayerWindow(object):
    def setupUi(self, PlayerWindow):
        if not PlayerWindow.objectName():
            PlayerWindow.setObjectName(u"PlayerWindow")
        PlayerWindow.resize(400, 300)
        self.centralwidget = QWidget(PlayerWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelLogo = QLabel(self.centralwidget)
        self.labelLogo.setObjectName(u"labelLogo")
        self.labelLogo.setPixmap(QPixmap(u":/recursos/logo.png"))
        self.labelLogo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelLogo)

        self.btnReproducir = QPushButton(self.centralwidget)
        self.btnReproducir.setObjectName(u"btnReproducir")
        icon = QIcon()
        icon.addFile(u":/recursos/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnReproducir.setIcon(icon)

        self.verticalLayout.addWidget(self.btnReproducir)

        PlayerWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PlayerWindow)

        QMetaObject.connectSlotsByName(PlayerWindow)
    # setupUi

    def retranslateUi(self, PlayerWindow):
        PlayerWindow.setWindowTitle(QCoreApplication.translate("PlayerWindow", u"Proyecto QRC", None))
        self.btnReproducir.setText(QCoreApplication.translate("PlayerWindow", u"Reproducir", None))
    # retranslateUi

