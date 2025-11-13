import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QLineEdit, QScrollArea, QToolBar, QMessageBox, QMainWindow
)
from PySide6.QtGui import QAction, QPixmap, QIcon
from PySide6.QtCore import Qt


# --- Componente Producto ---
class ProductoConIcono(QWidget):
    def __init__(self, nombre: str, precio: str, icono_path: str = "icons/laptop.png", parent=None):
        super().__init__(parent)

        # Icono
        self.__icono_lbl = QLabel()
        self.__icono_lbl.setFixedSize(60, 60)
        self.__icono_lbl.setScaledContents(True)
        self.__icono_lbl.setPixmap(QPixmap(icono_path))

        # Textos
        self.__nombre_lbl = QLabel(nombre)
        self.__precio_lbl = QLabel(precio)

        # Layout vertical para textos
        texto_layout = QVBoxLayout()
        texto_layout.addWidget(self.__nombre_lbl)
        texto_layout.addWidget(self.__precio_lbl)

        # Layout horizontal principal
        layout = QHBoxLayout(self)
        layout.addWidget(self.__icono_lbl)
        layout.addLayout(texto_layout)

        # Datos
        self.nombre = nombre

    def setVisibleFiltro(self, visible: bool):
        self.setVisible(visible)

# --- Ventana Principal ---
class TechMarketDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TechMarket Dashboard")
        self.resize(500, 400)

        # Barra de estado
        self.statusBar().showMessage("Listo")

        # --- Toolbar ---
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        btn_add = QAction("Añadir producto", self)
        btn_del = QAction("Eliminar producto", self)
        btn_stats = QAction("Mostrar estadísticas", self)

        toolbar.addAction(btn_add)
        toolbar.addAction(btn_del)
        toolbar.addAction(btn_stats)

        # --- Señales ---
        btn_stats.triggered.connect(self.mostrar_estadisticas)
        btn_add.triggered.connect(self.añadir_producto)
        btn_del.triggered.connect(self.eliminar_producto)

        # --- Widget central ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_layout = QVBoxLayout(central_widget)

        # Buscador
        self.buscador = QLineEdit()
        self.buscador.setPlaceholderText("Buscar producto...")
        self.buscador.textChanged.connect(self.filtrar_productos)
        central_layout.addWidget(self.buscador)

        # Scroll area para productos
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        central_layout.addWidget(self.scroll_area)

        self.productos_container = QWidget()
        self.productos_layout = QVBoxLayout(self.productos_container)
        self.productos_layout.setAlignment(Qt.AlignTop)

        self.scroll_area.setWidget(self.productos_container)

        # Lista de productos
        self.productos = []
        self.cargar_productos_ejemplo()

    # --- Métodos ---
    def cargar_productos_ejemplo(self):
        ejemplos = [
            ("Portátil ZenAir", "799 €", "icons/laptop.png"),
            ("Ratón Ergonomic", "25 €", "icons/mouse.png"),
            ("Teclado Gamer RGB", "99 €", "icons/keyboard.png")
        ]
        for nombre, precio, icono in ejemplos:
            prod = ProductoConIcono(nombre, precio, icono)
            self.productos.append(prod)
            self.productos_layout.addWidget(prod)

    def filtrar_productos(self, texto):
        texto = texto.lower()
        for prod in self.productos:
            visible = texto in prod.nombre.lower() or texto == ""
            prod.setVisibleFiltro(visible)

    def mostrar_estadisticas(self):
        total = len(self.productos)
        visibles = sum(1 for p in self.productos if p.isVisible())
        QMessageBox.information(self, "Estadísticas",
                                f"Total de productos: {total}\nProductos visibles: {visibles}")

    def añadir_producto(self):
        # Solo un ejemplo simple
        prod = ProductoConIcono("Nuevo Producto", "0 €", "icons/laptop.png")
        self.productos.append(prod)
        self.productos_layout.addWidget(prod)
        self.statusBar().showMessage("Producto añadido", 2000)

    def eliminar_producto(self):
        if self.productos:
            prod = self.productos.pop()
            prod.setParent(None)
            prod.deleteLater()
            self.statusBar().showMessage("Producto eliminado", 2000)
        else:
            self.statusBar().showMessage("No hay productos para eliminar", 2000)

# --- Ejecutar ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = TechMarketDashboard()
    ventana.show()
    sys.exit(app.exec())
