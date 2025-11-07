from PySide6.QtWidgets import QWidget, QVBoxLayout, QSlider, QLabel
from PySide6.QtGui import QPainter, QColor, QBrush, QPen
from PySide6.QtCore import Qt

class BatteryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._level = 50
        self.setMinimumSize(150, 50)
    def setLevel(self, val):
        self._level = max(0, min(100, val)); self.update()
    def paintEvent(self, e):
        p = QPainter(self)
        p.setPen(QPen(Qt.black, 2))
        p.drawRect(10, 10, 120, 30)
        color = QColor("red") if self._level<20 else QColor("green")
        p.setBrush(QBrush(color))
        p.drawRect(12, 12, int(1.16*self._level), 26)
        p.setBrush(QBrush(Qt.black))
        p.drawRect(132, 20, 6, 10)

class BatteryDemo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.battery = BatteryWidget()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,100); self.slider.setValue(50)
        self.lbl = QLabel("Nivel: 50%")
        self.slider.valueChanged.connect(lambda v:(self.battery.setLevel(v), self.lbl.setText(f"Nivel: {v}%")))
        layout.addWidget(self.battery)
        layout.addWidget(self.slider)
        layout.addWidget(self.lbl)
