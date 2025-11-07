import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QStatusBar
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

from t1_switch import SwitchWidget
from t2_moneylineedit import MoneyWidget
from t3_batterywidget import BatteryDemo
from t4_searchinput import SearchWidget
import recursos_rc  # generado con pyside6-rcc


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🏢 CustomWidgetsCompany")
        self.setWindowIcon(QIcon(":/icons/company.png"))
        self.resize(500, 400)

        # Pestañas principales
        tabs = QTabWidget()
        tabs.addTab(SwitchWidget(), "🔘 Switch")
        tabs.addTab(MoneyWidget(), "💶 Money LineEdit")
        tabs.addTab(BatteryDemo(), "🔋 Battery Widget")
        tabs.addTab(SearchWidget(), "🔍 Search Input")

        # Barra de estado
        status = QStatusBar()
        status.showMessage("Listo")
        self.setStatusBar(status)

        # Asignar contenido central
        self.setCentralWidget(tabs)

        # Aplicar estilos generales
        self.setStyleSheet("""
            QWidget {
                font-family: 'Segoe UI';
                font-size: 12pt;
            }

            QTabWidget::pane {
                border: 2px solid #2980b9;
                border-radius: 8px;
                background: #fdfdfd;
                margin-top: -1px;
            }

            QTabBar::tab {
                background: #ecf0f1;
                border: 1px solid #bdc3c7;
                padding: 8px 16px;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                margin-right: 2px;
            }

            QTabBar::tab:selected {
                background: #3498db;
                color: white;
                border: 1px solid #2980b9;
            }

            QStatusBar {
                background: #f0f0f0;
                color: #2980b9;
                font-style: italic;
                padding-left: 10px;
            }

            QToolButton {
                background: #e0e0e0;
                border: none;
                border-radius: 5px;
                padding: 4px;
                font-weight: bold;
            }
            QToolButton:hover {
                background: #d5d5d5;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
