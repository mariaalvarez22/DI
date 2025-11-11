# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mini1.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit_busqueda = QLineEdit(Form)
        self.lineEdit_busqueda.setObjectName(u"lineEdit_busqueda")

        self.verticalLayout.addWidget(self.lineEdit_busqueda)

        self.label_producto1 = QLabel(Form)
        self.label_producto1.setObjectName(u"label_producto1")

        self.verticalLayout.addWidget(self.label_producto1)

        self.label_producto2 = QLabel(Form)
        self.label_producto2.setObjectName(u"label_producto2")

        self.verticalLayout.addWidget(self.label_producto2)

        self.label_producto3 = QLabel(Form)
        self.label_producto3.setObjectName(u"label_producto3")

        self.verticalLayout.addWidget(self.label_producto3)

        self.label_producto4 = QLabel(Form)
        self.label_producto4.setObjectName(u"label_producto4")

        self.verticalLayout.addWidget(self.label_producto4)

        self.label_producto5 = QLabel(Form)
        self.label_producto5.setObjectName(u"label_producto5")

        self.verticalLayout.addWidget(self.label_producto5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Mini 1 \u2013 Buscador de productos", None))
        self.lineEdit_busqueda.setPlaceholderText(QCoreApplication.translate("Form", u"Escribe para buscar...", None))
        self.label_producto1.setText(QCoreApplication.translate("Form", u"Port\u00e1til ZenAir", None))
        self.label_producto2.setText(QCoreApplication.translate("Form", u"Rat\u00f3n \u00d3ptico Pro", None))
        self.label_producto3.setText(QCoreApplication.translate("Form", u"Teclado Mec\u00e1nico RGB", None))
        self.label_producto4.setText(QCoreApplication.translate("Form", u"Auriculares Bass+", None))
        self.label_producto5.setText(QCoreApplication.translate("Form", u"Monitor UltraWide", None))
    # retranslateUi

