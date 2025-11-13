from PySide6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QToolButton

class SearchInput(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # Sin márgenes, para verse más limpio

        # Campo de texto con placeholder
        self.text = QLineEdit(placeholderText="Buscar…")

        # Botón con una X para limpiar el texto
        self.btn = QToolButton(text="✖")
        self.btn.setToolTip("Limpiar texto")
        self.btn.clicked.connect(self.text.clear)

        # Añadir los widgets al layout
        layout.addWidget(self.text)
        layout.addWidget(self.btn)

        self.setLayout(layout)
