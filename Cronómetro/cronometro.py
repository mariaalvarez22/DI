from PySide6.QtCore import QElapsedTimer, QTime

class Cronometro:
    def __init__(self):
        self._tiempo_transcurrido = QElapsedTimer()
        self._tiempo_pausa = QElapsedTimer()
        self.acumulador = 0  # tiempo total pausado

    def reiniciar(self):
        # Reinicia todo a cero
        self._tiempo_transcurrido.restart()
        self.acumulador = 0

    def pausar(self):
        # Comienza a medir la pausa
        self._tiempo_pausa.restart()

    def continuar(self):
        # Suma al acumulador el tiempo que estuvo en pausa
        self.acumulador += self._tiempo_pausa.elapsed()

    def getTime(self):
        # Tiempo total transcurrido (sin contar pausas)
        return QTime(0, 0).addMSecs(self._tiempo_transcurrido.elapsed() - self.acumulador)
