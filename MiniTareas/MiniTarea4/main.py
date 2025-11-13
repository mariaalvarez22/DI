import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QPixmap
import resources_rc  # 🔹 importa el archivo generado por pyside6-rcc


class ProductoConIcono(QWidget):
    """
    Clase que representa un producto con su icono, nombre y precio.
    """
    def __init__(self, nombre: str, precio: str, icono_path: str = "icons/laptop.png", parent=None):
        super().__init__(parent)

        # --- Icono ---
        self.__icono_lbl = QLabel()
        self.__icono_lbl.setFixedSize(60, 60)
        self.__icono_lbl.setScaledContents(True)
        self.__icono_lbl.setPixmap(QPixmap(icono_path))

        # --- Textos ---
        self.__nombre_lbl = QLabel(nombre)
        self.__precio_lbl = QLabel(precio)

        # Layout para textos (vertical)
        texto_layout = QVBoxLayout()
        texto_layout.addWidget(self.__nombre_lbl)
        texto_layout.addWidget(self.__precio_lbl)

        # Layout principal (horizontal)
        layout = QHBoxLayout(self)
        layout.addWidget(self.__icono_lbl)
        layout.addLayout(texto_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = QWidget()
    ventana.setWindowTitle("Mini 4 – Productos con icono")

    layout = QVBoxLayout(ventana)

    # --- Tres productos con iconos distintos ---
    layout.addWidget(ProductoConIcono("Portátil ZenAir", "799 €", icono_path="icons/laptop.png"))
    layout.addWidget(ProductoConIcono("Ratón Ergonomic", "25 €", icono_path="icons/mouse.png"))
    layout.addWidget(ProductoConIcono("Teclado Gamer RGB", "99 €", icono_path="icons/keyboard.png"))

    ventana.show()
    sys.exit(app.exec())
