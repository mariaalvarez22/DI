# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Calculadora.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.display = QLineEdit(self.centralwidget)
        self.display.setObjectName(u"display")
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        font = QFont()
        font.setPointSize(24)
        self.display.setFont(font)

        self.verticalLayout.addWidget(self.display)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn7 = QPushButton(self.centralwidget)
        self.btn7.setObjectName(u"btn7")

        self.gridLayout.addWidget(self.btn7, 0, 0, 1, 1)

        self.btn8 = QPushButton(self.centralwidget)
        self.btn8.setObjectName(u"btn8")

        self.gridLayout.addWidget(self.btn8, 0, 1, 1, 1)

        self.btn9 = QPushButton(self.centralwidget)
        self.btn9.setObjectName(u"btn9")

        self.gridLayout.addWidget(self.btn9, 0, 2, 1, 1)

        self.btnDivision = QPushButton(self.centralwidget)
        self.btnDivision.setObjectName(u"btnDivision")

        self.gridLayout.addWidget(self.btnDivision, 0, 3, 1, 1)

        self.btn4 = QPushButton(self.centralwidget)
        self.btn4.setObjectName(u"btn4")

        self.gridLayout.addWidget(self.btn4, 1, 0, 1, 1)

        self.btn5 = QPushButton(self.centralwidget)
        self.btn5.setObjectName(u"btn5")

        self.gridLayout.addWidget(self.btn5, 1, 1, 1, 1)

        self.btn6 = QPushButton(self.centralwidget)
        self.btn6.setObjectName(u"btn6")

        self.gridLayout.addWidget(self.btn6, 1, 2, 1, 1)

        self.btnMultiplicacion = QPushButton(self.centralwidget)
        self.btnMultiplicacion.setObjectName(u"btnMultiplicacion")

        self.gridLayout.addWidget(self.btnMultiplicacion, 1, 3, 1, 1)

        self.btn1 = QPushButton(self.centralwidget)
        self.btn1.setObjectName(u"btn1")

        self.gridLayout.addWidget(self.btn1, 2, 0, 1, 1)

        self.btn2 = QPushButton(self.centralwidget)
        self.btn2.setObjectName(u"btn2")

        self.gridLayout.addWidget(self.btn2, 2, 1, 1, 1)

        self.btn3 = QPushButton(self.centralwidget)
        self.btn3.setObjectName(u"btn3")

        self.gridLayout.addWidget(self.btn3, 2, 2, 1, 1)

        self.btnResta = QPushButton(self.centralwidget)
        self.btnResta.setObjectName(u"btnResta")

        self.gridLayout.addWidget(self.btnResta, 2, 3, 1, 1)

        self.btn0 = QPushButton(self.centralwidget)
        self.btn0.setObjectName(u"btn0")

        self.gridLayout.addWidget(self.btn0, 3, 0, 1, 1)

        self.btnC = QPushButton(self.centralwidget)
        self.btnC.setObjectName(u"btnC")

        self.gridLayout.addWidget(self.btnC, 3, 1, 1, 1)

        self.btnIgual = QPushButton(self.centralwidget)
        self.btnIgual.setObjectName(u"btnIgual")

        self.gridLayout.addWidget(self.btnIgual, 3, 2, 1, 1)

        self.btnSuma = QPushButton(self.centralwidget)
        self.btnSuma.setObjectName(u"btnSuma")

        self.gridLayout.addWidget(self.btnSuma, 3, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculadora", None))
        self.btn7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btnDivision.setText(QCoreApplication.translate("MainWindow", u"÷", None))
        self.btn4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btnMultiplicacion.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.btn1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btnResta.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnC.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btnIgual.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btnSuma.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi

