import sys
from PySide6.QtWidgets import QApplication, QWidget
from mini1_ui import Ui_Form

class Buscador(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()   # ← aquí cambia
        self.ui.setupUi(self)

        # Lista de productos y labels
        self.productos = [
            "Portátil ZenAir",
            "Ratón Óptico Pro",
            "Teclado Mecánico RGB",
            "Auriculares Bass+",
            "Monitor UltraWide"
        ]
        self.labels = [
            self.ui.label_producto1,
            self.ui.label_producto2,
            self.ui.label_producto3,
            self.ui.label_producto4,
            self.ui.label_producto5
        ]

        # Conectar el QLineEdit a la función de filtrado
        self.ui.lineEdit_busqueda.textChanged.connect(self.filtrar_productos)

    def filtrar_productos(self, texto):
        texto = texto.lower()
        for producto, label in zip(self.productos, self.labels):
            if texto in producto.lower() or texto == "":
                label.show()
            else:
                label.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Buscador()
    ventana.show()
    sys.exit(app.exec())
