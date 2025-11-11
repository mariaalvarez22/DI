import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QFrame
)


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

        # Estilo opcional (para diferenciar los productos)
        self.label_nombre.setStyleSheet("font-weight: bold; font-size: 14px;")
        self.label_precio.setStyleSheet("color: green; font-size: 12px;")

        self.layout.addWidget(self.label_nombre)
        self.layout.addWidget(self.label_precio)
        self.setStyleSheet("""
            QWidget {
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 6px;
                background-color: #f9f9f9;
            }
        """)

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



class ListaProductos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini 3 – Catálogo con buscador")

        layout_principal = QVBoxLayout(self)

        # --- Campo de búsqueda ---
        self.buscador = QLineEdit()
        self.buscador.setPlaceholderText("Buscar producto...")
        self.buscador.textChanged.connect(self.filtrar_productos)
        layout_principal.addWidget(self.buscador)

        # --- Scroll con los productos ---
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        layout_principal.addWidget(self.scroll_area)

        # Contenedor interno dentro del scroll
        self.contenedor = QWidget()
        self.layout_productos = QVBoxLayout(self.contenedor)

        # Lista de productos inicial
        self.lista_productos = [
            Producto("Portátil ZenAir", "799 €"),
            Producto("Ratón Ergonomic", "25 €"),
            Producto("Teclado Gamer RGB", "99 €"),
            Producto("Monitor Curvo 27''", "249 €"),
            Producto("Webcam 4K", "120 €")
        ]

        # Añadir los productos al layout
        for producto in self.lista_productos:
            self.layout_productos.addWidget(producto)

        # Pequeño espacio al final
        self.layout_productos.addStretch()

        # Asignar contenedor al scroll
        self.scroll_area.setWidget(self.contenedor)

 
    def filtrar_productos(self, texto):
        texto = texto.lower().strip()
        for producto in self.lista_productos:
            producto.setVisible(texto in producto.nombre.lower() or texto == "")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ListaProductos()
    ventana.resize(300, 400)
    ventana.show()
    sys.exit(app.exec())
