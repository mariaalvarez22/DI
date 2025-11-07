import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from t4_searchinput import SearchInput

app = QApplication(sys.argv)

# Ventana principal
w = QWidget()
w.setWindowTitle("Mini-tarea 4 — SearchInput")

v = QVBoxLayout(w)

# Crear el buscador y la etiqueta de contador
s = SearchInput()
lbl = QLabel("0 caracteres")

# Conectar el texto del buscador con la etiqueta
s.text.textChanged.connect(lambda t: lbl.setText(f"{len(t)} caracteres"))

# Añadir al layout
v.addWidget(s)
v.addWidget(lbl)

w.setLayout(v)
w.show()

app.exec()
