from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit
from PySide6.QtCore import Signal

class MoneyLineEdit(QLineEdit):
    valueChanged = Signal(float)
    def __init__(self):
        super().__init__()
        self.textChanged.connect(self.on_text_changed)
    def on_text_changed(self, txt):
        try:
            val = float(txt.replace(",", "."))
            self.valueChanged.emit(val)
        except:
            pass

class MoneyWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.txt = MoneyLineEdit()
        self.lbl = QLabel("Valor:")
        self.txt.valueChanged.connect(lambda v: self.lbl.setText(f"Valor: {v:.2f} €"))
        layout.addWidget(self.txt)
        layout.addWidget(self.lbl)
