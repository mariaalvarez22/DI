# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Nortempo.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 784)
        MainWindow.setMinimumSize(QSize(5, 11))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.act_Informacion = QAction(MainWindow)
        self.act_Informacion.setObjectName(u"act_Informacion")
        icon = QIcon()
        icon.addFile(u"IconoInfo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.act_Informacion.setIcon(icon)
        self.act_Informacion.setMenuRole(QAction.MenuRole.NoRole)
        self.action_Contacto = QAction(MainWindow)
        self.action_Contacto.setObjectName(u"action_Contacto")
        icon1 = QIcon()
        icon1.addFile(u"iconoContacto.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_Contacto.setIcon(icon1)
        self.action_Contacto.setMenuRole(QAction.MenuRole.NoRole)
        self.actionVolver_al_Inicio = QAction(MainWindow)
        self.actionVolver_al_Inicio.setObjectName(u"actionVolver_al_Inicio")
        icon2 = QIcon()
        icon2.addFile(u"IconoVolver.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionVolver_al_Inicio.setIcon(icon2)
        self.actionVolver_al_Inicio.setMenuRole(QAction.MenuRole.NoRole)
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        icon3 = QIcon()
        icon3.addFile(u"IconoSalir.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionSalir.setIcon(icon3)
        self.actionSalir.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuDar_de_comer = QMenu(self.menubar)
        self.menuDar_de_comer.setObjectName(u"menuDar_de_comer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QSize(5, 0))
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuDar_de_comer.menuAction())
        self.menuDar_de_comer.addAction(self.act_Informacion)
        self.menuDar_de_comer.addAction(self.action_Contacto)
        self.menuDar_de_comer.addAction(self.actionVolver_al_Inicio)
        self.menuDar_de_comer.addAction(self.actionSalir)
        self.toolBar.addAction(self.act_Informacion)
        self.toolBar.addAction(self.action_Contacto)
        self.toolBar.addAction(self.actionVolver_al_Inicio)
        self.toolBar.addAction(self.actionSalir)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(QCoreApplication.translate("MainWindow", u"Salir de la aplicacion", None))
#endif // QT_CONFIG(tooltip)
        self.act_Informacion.setText(QCoreApplication.translate("MainWindow", u"Informacion DAM/DAW", None))
        self.action_Contacto.setText(QCoreApplication.translate("MainWindow", u"Contacto", None))
        self.actionVolver_al_Inicio.setText(QCoreApplication.translate("MainWindow", u"Volver al Inicio        ", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
#if QT_CONFIG(shortcut)
        self.actionSalir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.menuDar_de_comer.setTitle(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

