import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

# Importante: este archivo se genera con pyside6-rcc
import recursos_rc

app = QApplication(sys.argv)
loader = QUiLoader()

# Carga el archivo .ui creado con Qt Designer
f = QFile("interfaz.ui")
f.open(QFile.ReadOnly)
window = loader.load(f)
f.close()

# Opcional: centra la ventana y pone un tamaño fijo
window.resize(500, 350)
window.setFixedSize(window.size())

window.show()
app.exec()
