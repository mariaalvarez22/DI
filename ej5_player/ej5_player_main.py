# main.py
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QStringListModel
from ej5_player import Ui_MainWindow
import sys

class Player(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Crear modelo para la lista de canciones
        self.model = QStringListModel()
        self.model.setStringList(["Canción 1", "Canción 2", "Canción 3"])
        self.ui.listView.setModel(self.model)

        # Conectar acciones del menú y toolbar
        self.ui.actionSalir.triggered.connect(self.close)
        self.ui.actionAbrir.triggered.connect(self.abrirArchivo)
        self.ui.actionActPlay.triggered.connect(lambda: self.ui.statusbar.showMessage("Play"))
        self.ui.actionActPause.triggered.connect(lambda: self.ui.statusbar.showMessage("Pause"))
        self.ui.actionActStop.triggered.connect(lambda: self.ui.statusbar.showMessage("Stop"))

        # Doble clic en la lista para cambiar el título
        self.ui.listView.doubleClicked.connect(self.cambiarTitulo)

    def abrirArchivo(self):
        archivo, _ = QFileDialog.getOpenFileName(self, "Abrir archivo")
        if archivo:
            self.ui.statusbar.showMessage(f"Abriste: {archivo}")

    def cambiarTitulo(self, index):
        texto = self.model.data(index)
        self.ui.lblTitulo.setText(texto)
        self.ui.statusbar.showMessage(f"Título cambiado a: {texto}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Player()
    ventana.show()
    sys.exit(app.exec())



