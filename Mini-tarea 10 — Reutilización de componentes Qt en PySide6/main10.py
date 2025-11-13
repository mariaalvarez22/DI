import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget
from PySide6.QtGui import QIcon
import resources_rc  # importa el archivo de recursos generado

from componentes.boton_saludador import BotonSaludador
from componentes.panel_empleados import PanelEmpleados

class MiniTarea10(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini-tarea 10 – Reutilización de componentes")

        # Icono de la app desde recursos
        self.setWindowIcon(QIcon("icons/app_icon.png"))

        # Pestañas
        tabs = QTabWidget()
        self.setCentralWidget(tabs)

        # Pestaña 1: BotonSaludador
        tabs.addTab(BotonSaludador(), "Saludador")

        # Pestaña 2: PanelEmpleados
        tabs.addTab(PanelEmpleados(), "Empleados")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiniTarea10()
    ventana.resize(400, 300)
    ventana.show()
    sys.exit(app.exec())
