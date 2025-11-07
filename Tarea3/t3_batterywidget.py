from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QBrush, QPen
from PySide6.QtCore import Qt


class BatteryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._level = 50  # Nivel inicial (50%)
        self.setMinimumSize(150, 50)

    def setLevel(self, val: int):
        """Actualiza el nivel de batería y redibuja el widget."""
        self._level = max(0, min(100, val))
        self.update()

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        # Marco de la batería
        p.setPen(QPen(Qt.black, 2))
        p.drawRect(10, 10, 120, 30)

        # Color según el nivel
        color = QColor("red") if self._level < 20 else QColor("green")
        p.setBrush(QBrush(color))

        # Nivel de carga
        p.drawRect(12, 12, int(1.16 * self._level), 26)

        # Terminal de la batería (parte derecha)
        p.setBrush(QBrush(Qt.black))
        p.drawRect(132, 20, 6, 10)
