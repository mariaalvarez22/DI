# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Repaso8.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1208, 645)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(300, 130, 120, 80))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 30, 49, 16))
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 40, 49, 16))
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 49, 16))
        self.stackedWidget.addWidget(self.page_2)
        self.Boton1 = QPushButton(self.centralwidget)
        self.Boton1.setObjectName(u"Boton1")
        self.Boton1.setGeometry(QRect(300, 250, 79, 24))
        self.boton2 = QPushButton(self.centralwidget)
        self.boton2.setObjectName(u"boton2")
        self.boton2.setGeometry(QRect(420, 260, 79, 24))
        self.Boton3 = QPushButton(self.centralwidget)
        self.Boton3.setObjectName(u"Boton3")
        self.Boton3.setGeometry(QRect(550, 250, 79, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1208, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"capa2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"capa3", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Capa1", None))
        self.Boton1.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.boton2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Boton3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

