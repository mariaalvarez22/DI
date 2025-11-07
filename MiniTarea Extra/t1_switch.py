from PySide6.QtWidgets import QWidget, QVBoxLayout, QCheckBox

class SwitchWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.chkSwitch = QCheckBox("OFF")
        self.chkSwitch.setStyleSheet("""
        QCheckBox::indicator { width:46px; height:24px; }
        QCheckBox::indicator:unchecked { border-radius:12px; background:#ccc; }
        QCheckBox::indicator:checked { border-radius:12px; background:#2ecc71; }
        """)
        self.chkSwitch.toggled.connect(lambda s: self.chkSwitch.setText("ON" if s else "OFF"))
        layout.addWidget(self.chkSwitch)
