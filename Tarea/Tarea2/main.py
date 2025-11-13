from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from t2_moneylineedit import MoneyLineEdit
import sys

app = QApplication(sys.argv)

# Ventana principal
w = QWidget()
w.setWindowTitle("MoneyLineEdit Demo")

layout = QVBoxLayout(w)

# Instanciamos el widget personalizado
txt = MoneyLineEdit()
lbl = QLabel("Valor:")

# Conectamos la señal personalizada al QLabel
txt.valueChanged.connect(lambda v: lbl.setText(f"Valor: {v:.2f} €"))

# Añadimos widgets al layout
layout.addWidget(txt)
layout.addWidget(lbl)

w.setLayout(layout)
w.show()

# Ejecutar la aplicación
app.exec()
