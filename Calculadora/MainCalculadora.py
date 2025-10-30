from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QGridLayout, QWidget
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

# -------- Lógica de la Calculadora ---------
class Calculadora:
    def __init__(self):
        self.valor_actual = ""
        self.valor_anterior = None
        self.operacion = None

    def agregar_numero(self, numero):
        self.valor_actual += str(numero)

    def agregar_operacion(self, op):
        if self.valor_actual:
            if self.valor_anterior is not None:
                self.calcular()
            self.valor_anterior = float(self.valor_actual)
            self.valor_actual = ""
            self.operacion = op

    def limpiar(self):
        self.valor_actual = ""
        self.valor_anterior = None
        self.operacion = None

    def calcular(self):
        if self.valor_anterior is not None and self.valor_actual and self.operacion:
            try:
                num_actual = float(self.valor_actual)
                if self.operacion == "+":
                    resultado = self.valor_anterior + num_actual
                elif self.operacion == "-":
                    resultado = self.valor_anterior - num_actual
                elif self.operacion == "*":
                    resultado = self.valor_anterior * num_actual
                elif self.operacion == "/":
                    if num_actual == 0:
                        return "Error"
                    resultado = self.valor_anterior / num_actual

                self.valor_actual = str(resultado)
                self.valor_anterior = None
                self.operacion = None
                return self.valor_actual
            except:
                return "Error"
        return self.valor_actual

# ---- Interfaz de la Calculadora ------
class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.calc = Calculadora()
        self.setWindowTitle("MERYS CALCULATOR")
        self.setFixedSize(420, 550)

        self.valor_actual = ""
        self.init_ui()
        self.aplicar_estilos()

    def init_ui(self):
        # Widget central y layout
        self.central = QWidget()
        self.setCentralWidget(self.central)
        self.verticalLayout = QVBoxLayout(self.central)
        self.verticalLayout.setSpacing(5)

        # Display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.display.setFont(QFont("Arial", 32))
        self.verticalLayout.addWidget(self.display)

        # Grid de botones
        self.gridLayout = QGridLayout()
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(5)
        self.verticalLayout.addLayout(self.gridLayout)

        # Botones
        botones = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]

        self.botones_dict = {}
        for text, row, col in botones:
            btn = QPushButton(text)
            btn.setFont(QFont("Arial", 26))
            self.gridLayout.addWidget(btn, row, col)
            self.botones_dict[text] = btn
            btn.clicked.connect(lambda checked, t=text: self.boton_presionado(t))

    def aplicar_estilos(self):
        # Display
        self.display.setStyleSheet("""
            background-color: #fffae3;
            color: #222831;
            border-radius: 10px;
            padding: 10px;
        """)

        # Estilo botones
        estilo_numero = """
            QPushButton {
                background-color: #ffca3a;
                color: #222831;
                border-radius: 20px;
                min-width: 80px;
                min-height: 80px;
            }
            QPushButton:hover { background-color: #ffd60a; }
            QPushButton:pressed { background-color: #e6b800; }
        """
        estilo_operacion = """
            QPushButton {
                background-color: #8ac926;
                color: #ffffff;
                border-radius: 20px;
                min-width: 80px;
                min-height: 80px;
            }
            QPushButton:hover { background-color: #6fbf00; }
            QPushButton:pressed { background-color: #5ea200; }
        """
        estilo_c = """
            QPushButton {
                background-color: #ff595e;
                color: #ffffff;
                border-radius: 20px;
                min-width: 80px;
                min-height: 80px;
            }
            QPushButton:hover { background-color: #ff2e3c; }
            QPushButton:pressed { background-color: #e60023; }
        """

        for text, btn in self.botones_dict.items():
            if text.isdigit():
                btn.setStyleSheet(estilo_numero)
            elif text in '+-*/=':
                btn.setStyleSheet(estilo_operacion)
            else:  # 'C'
                btn.setStyleSheet(estilo_c)

    def boton_presionado(self, texto):
        if texto == 'C':
            self.calc.limpiar()
        elif texto == '=':
            resultado = self.calc.calcular()
            self.display.setText(str(resultado))
            return
        else:
            self.calc.agregar_numero(texto) if texto.isdigit() else self.calc.agregar_operacion(texto)
        self.display.setText(self.calc.valor_actual)

if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec()
