from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Signal

class MoneyLineEdit(QLineEdit):
    # Señal personalizada que emite un float cuando el texto cambia
    valueChanged = Signal(float)

    def __init__(self, parent=None):
        super().__init__(parent)
        # Conectamos el evento de texto cambiado a nuestro método
        self.textChanged.connect(self.on_text_changed)

    def on_text_changed(self, txt):
        """Convierte el texto en número y emite la señal si es válido."""
        try:
            # Permite escribir con coma o punto decimal
            val = float(txt.replace(",", "."))
            self.valueChanged.emit(val)
        except ValueError:
            # Si no es un número, no hace nada
            pass
