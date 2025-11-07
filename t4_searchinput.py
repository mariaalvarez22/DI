from PySide6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QToolButton, QVBoxLayout, QLabel

class SearchInput(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        self.text = QLineEdit(placeholderText="Buscar…")
        self.btn = QToolButton(text="✖")
        self.btn.clicked.connect(self.text.clear)
        layout.addWidget(self.text)
        layout.addWidget(self.btn)

class SearchWidget(QWidget):
    def __init__(self):
        super().__init__()
        v = QVBoxLayout(self)
        self.search = SearchInput()
        self.lbl = QLabel("0 caracteres")
        self.search.text.textChanged.connect(lambda t: self.lbl.setText(f"{len(t)} caracteres"))
        v.addWidget(self.search)
        v.addWidget(self.lbl)
