import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PySide6.QtGui import QPixmap
import resources_rc  # importa el fichero generado por pyside6-rcc


class EmpresaConIcono(QWidget):
    """
    Variante de 'Empresa' que añade un logo usando recursos Qt (:/icons/...)
    """
    def __init__(self, nombre: str, direccion: str, icono_path: str = ":/icons/logo1.png", parent=None):
        super().__init__(parent)

        # (1) Logo
        self.__logo_lbl = QLabel()
        self.__logo_lbl.setFixedSize(60, 60)
        self.__logo_lbl.setScaledContents(True)
        self.__logo_lbl.setPixmap(QPixmap(icono_path))

        # (2) Textos
        self.__nombre_lbl = QLabel(nombre)
        self.__direccion_lbl = QLabel(direccion)

        textos = QVBoxLayout()
        textos.addWidget(self.__nombre_lbl)
        textos.addWidget(self.__direccion_lbl)

        # (3) Layout final
        root = QHBoxLayout(self)
        root.addWidget(self.__logo_lbl)
        root.addLayout(textos)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle("Mini 4 - Empresa con icono (recursos Qt)")
    lay = QVBoxLayout(w)

    lay.addWidget(EmpresaConIcono("PinApple", "C/ Sin nombre, 00000", icono_path=":/icons/logo1.png"))
    lay.addWidget(EmpresaConIcono("Toogle", "C/ Sin hielo, 33333", icono_path=":/icons/logo2.png"))

    w.show()
    app.exec()
