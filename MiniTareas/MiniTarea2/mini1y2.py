import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QFrame

class Buscador(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini 1 – Buscador de productos")

        # Lista de productos
        self.productos = [
            "Portátil ZenAir",
            "Ratón Óptico Pro",
            "Teclado Mecánico RGB",
            "Auriculares Bass+",
            "Monitor UltraWide"
        ]

        self.layout = QVBoxLayout(self)

        # Campo de texto para buscar
        self.buscador = QLineEdit()
        self.buscador.setPlaceholderText("Escribe para buscar un producto...")
        self.buscador.textChanged.connect(self.filtrar_productos)
        self.layout.addWidget(self.buscador)

        # Etiquetas con los nombres
        self.labels = []
        for producto in self.productos:
            label = QLabel(producto)
            self.layout.addWidget(label)
            self.labels.append(label)

    def filtrar_productos(self, texto):
        texto = texto.lower()
        for producto, label in zip(self.productos, self.labels):
            label.setVisible(texto in producto.lower() or texto == "")


class Producto(QWidget):
    def __init__(self, nombre, precio):
        super().__init__()

        # Atributos privados
        self._nombre = nombre
        self._precio = precio

        # Diseño
        self.layout = QVBoxLayout(self)
        self.label_nombre = QLabel(self._nombre)
        self.label_precio = QLabel(self._precio)

        self.layout.addWidget(self.label_nombre)
        self.layout.addWidget(self.label_precio)

    # Propiedad NOMBRE
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
        self.label_nombre.setText(valor)

    # Propiedad PRECIO
    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        self._precio = valor
        self.label_precio.setText(valor)


class DemoProducto(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini 2 – Componente Producto")

        self.layout = QVBoxLayout(self)

        # Creamos un producto inicial
        self.producto = Producto("Ratón Óptico Pro", "19,99 €")
        self.layout.addWidget(self.producto)

        # Botón que cambia el precio
        self.boton_actualizar = QPushButton("Actualizar precio")
        self.boton_actualizar.clicked.connect(self.actualizar_precio)
        self.layout.addWidget(self.boton_actualizar)

    def actualizar_precio(self):
        # Cambia el precio usando el setter
        self.producto.precio = "14,99 €"


class Mini1y2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini 1 y 2 – Buscador + Producto con @property")

        main_layout = QVBoxLayout(self)

        # --- Sección Mini 1 ---
        main_layout.addWidget(QLabel("<b>Mini 1 – Buscador de productos</b>"))
        self.buscador_widget = Buscador()
        main_layout.addWidget(self.buscador_widget)

        # Separador
        separador = QFrame()
        separador.setFrameShape(QFrame.HLine)
        separador.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(separador)

        # --- Sección Mini 2 ---
        main_layout.addWidget(QLabel("<b>Mini 2 – Componente Producto</b>"))
        self.demo_producto_widget = DemoProducto()
        main_layout.addWidget(self.demo_producto_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Mini1y2()
    ventana.show()
    sys.exit(app.exec())
