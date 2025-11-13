import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

# Clase Producto
class Producto(QWidget):
    def __init__(self, nombre, precio):
        super().__init__()

        self._nombre = nombre
        self._precio = precio

        self.layout = QVBoxLayout(self)

        self.label_nombre = QLabel(self._nombre)
        self.label_precio = QLabel(self._precio)

        self.layout.addWidget(self.label_nombre)
        self.layout.addWidget(self.label_precio)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
        self.label_nombre.setText(valor)

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        self._precio = valor
        self.label_precio.setText(valor)

# Ventana DemoProducto
class DemoProducto(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini 2 – Componente Producto")

        self.layout = QVBoxLayout(self)

        self.producto = Producto("Ratón Óptico Pro", "19,99 €")
        self.layout.addWidget(self.producto)

        self.boton_actualizar = QPushButton("Actualizar precio")
        self.boton_actualizar.clicked.connect(self.actualizar_precio)
        self.layout.addWidget(self.boton_actualizar)

    def actualizar_precio(self):
        self.producto.precio = "14,99 €"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = DemoProducto()
    ventana.show()
    sys.exit(app.exec())
