from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class PanelEmpleados(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)

        empleados = ["Ana", "Luis", "María", "Carlos"]
        for e in empleados:
            layout.addWidget(QLabel(f"Empleado: {e}"))
