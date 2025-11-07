import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel
from PySide6.QtCore import Qt
from t3_batterywidget import BatteryWidget


app = QApplication(sys.argv)

# Ventana principal
w = QWidget()
w.setWindowTitle("Mini-tarea 3 — Battery Widget")

layout = QVBoxLayout(w)

# Crear el widget de batería
battery = BatteryWidget()
slider = QSlider(Qt.Horizontal)
slider.setRange(0, 100)
slider.setValue(50)

# Etiqueta para mostrar el nivel numérico
lbl = QLabel("Nivel: 50%")
lbl.setAlignment(Qt.AlignCenter)

# Conectar el slider con el widget de batería
slider.valueChanged.connect(lambda val: (battery.setLevel(val), lbl.setText(f"Nivel: {val}%")))

# Añadir todo al layout
layout.addWidget(battery)
layout.addWidget(slider)
layout.addWidget(lbl)

w.setLayout(layout)
w.show()

sys.exit(app.exec())

