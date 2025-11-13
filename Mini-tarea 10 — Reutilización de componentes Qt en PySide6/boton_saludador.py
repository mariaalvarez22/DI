from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox

class BotonSaludador(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.boton = QPushButton("Saludar")
        self.boton.clicked.connect(self.mostrar_saludo)

        layout = QVBoxLayout(self)
        layout.addWidget(self.boton)

    def mostrar_saludo(self):
        QMessageBox.information(self, "Saludo", "¡Hola! Has pulsado el botón.")
