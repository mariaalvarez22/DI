from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import QTimer, Qt
from cronometro import Cronometro

class CronometroWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Lógica del cronómetro
        self.crono = Cronometro()

        # Etiqueta para mostrar tiempo
        self.label = QLabel("00:00:00")
        self.label.setAlignment(Qt.AlignCenter)

        # Botones
        self.btn_iniciar = QPushButton("Iniciar")
        self.btn_pausar = QPushButton("Pausar")
        self.btn_reanudar = QPushButton("Reanudar")
        self.btn_reiniciar = QPushButton("Reiniciar")

        # Layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn_iniciar)
        layout.addWidget(self.btn_pausar)
        layout.addWidget(self.btn_reanudar)
        layout.addWidget(self.btn_reiniciar)
        self.setLayout(layout)

        # Temporizador para actualizar cada segundo
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar)

        # Conexiones de botones
        self.btn_iniciar.clicked.connect(self.iniciar)
        self.btn_pausar.clicked.connect(self.pausar)
        self.btn_reanudar.clicked.connect(self.reanudar)
        self.btn_reiniciar.clicked.connect(self.reiniciar)

    def iniciar(self):
        # Inicia desde 0 siempre
        self.crono.reiniciar()
        self.timer.start(1000)

    def pausar(self):
        # Pausa el cronómetro
        if self.timer.isActive():
            self.crono.pausar()
            self.timer.stop()

    def reanudar(self):
        # Continúa desde donde se pausó
        self.crono.continuar()
        self.timer.start(1000)

    def reiniciar(self):
        # Reinicia todo a cero
        self.crono.reiniciar()
        self.label.setText("00:00:00")
        self.timer.stop()

    def actualizar(self):
        # Actualiza la etiqueta con el tiempo transcurrido
        tiempo = self.crono.getTime().toString("hh:mm:ss")
        self.label.setText(tiempo)
