import sys
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QMessageBox,
    QGraphicsScene,
    QGraphicsTextItem,
)
from PySide6.QtGui import QFont
from ui_mainwindow import Ui_MainWindow
from pypdf import PdfReader, PdfWriter

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Ruta actual del PDF cargado
        self.ruta_pdf = None

        # Configuración inicial
        self._configurar_interfaz()
        self._conectar_senales()

    # ================== CONFIGURACIÓN INICIAL ==================
    def _configurar_interfaz(self):
        self.setWindowTitle("Firma Digital de Documentos - DocuSecure")
        self.statusBar().showMessage("Listo: cargue un PDF para comenzar.")
        self._actualizar_preview("Ningún PDF cargado.")

    def _conectar_senales(self):
        # Botones
        self.btnExaminar.clicked.connect(self.on_examinar_pdf)
        self.btnFirmar.clicked.connect(self.on_firmar_pdf)

        # Menú Archivo
        self.actionAbrirPdf.triggered.connect(self.on_examinar_pdf)
        self.actionGuardarFirmado.triggered.connect(self.on_guardar_firmado)
        self.actionSalir.triggered.connect(self.close)

        # Menú Ayuda
        self.actionAcercaDe.triggered.connect(self.on_acerca_de)

    # ================== PREVISUALIZACIÓN ==================
    def _actualizar_preview(self, texto):
        escena = QGraphicsScene(self)
        item_texto = QGraphicsTextItem(texto)
        fuente = QFont()
        fuente.setPointSize(12)
        item_texto.setFont(fuente)
        escena.addItem(item_texto)
        self.gvPreview.setScene(escena)

    # ================== ACCIONES ==================
    def on_examinar_pdf(self):
        ruta, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar PDF",
            "",
            "Archivos PDF (*.pdf);;Todos los archivos (*)",
        )
        if not ruta:
            return  # Usuario canceló

        self.ruta_pdf = ruta
        self.leRutaPdf.setText(ruta)

        nombre_archivo = ruta.split("/")[-1].split("\\")[-1]
        self._actualizar_preview(f"PDF cargado:\n{nombre_archivo}")
        self.statusBar().showMessage(f"PDF cargado: {nombre_archivo}", 3000)

    def on_firmar_pdf(self):
        if not self.ruta_pdf:
            QMessageBox.warning(self, "Aviso", "Primero debes cargar un PDF.")
            return

        firmante = self.leFirmante.text().strip()
        motivo = self.leMotivo.text().strip()

        if not firmante:
            QMessageBox.warning(self, "Aviso", "Introduce el nombre del firmante.")
            return

        if not motivo:
            QMessageBox.warning(self, "Aviso", "Introduce el motivo de la firma.")
            return

        ruta_salida, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar PDF firmado",
            "documento_firmado.pdf",
            "Archivos PDF (*.pdf);;Todos los archivos (*)",
        )
        if not ruta_salida:
            return

        try:
            self._firmar_pdf(self.ruta_pdf, ruta_salida, firmante, motivo)
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error al firmar",
                f"Ocurrió un error al firmar el PDF:\n{e}",
            )
            return

        self.statusBar().showMessage(f"PDF firmado guardado en: {ruta_salida}", 5000)
        QMessageBox.information(
            self,
            "Firma completada",
            f"El PDF se ha firmado correctamente.\nRuta de salida:\n{ruta_salida}",
        )

    def _firmar_pdf(self, ruta_entrada, ruta_salida, firmante, motivo):
   
        reader = PdfReader(ruta_entrada)
        writer = PdfWriter()

        # Copiar páginas
        for page in reader.pages:
            writer.add_page(page)

        # Metadatos de firma
        fecha_firma = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        metadata = reader.metadata or {}
        metadata.update({
            "/SignedBy": firmante,
            "/SignatureReason": motivo,
            "/SignedAt": fecha_firma,
        })
        writer.add_metadata(metadata)

        # Guardar PDF firmado
        with open(ruta_salida, "wb") as f:
            writer.write(f)

    def on_guardar_firmado(self):
        QMessageBox.information(
            self,
            "Información",
            "Para guardar un PDF firmado, usa el botón 'Aplicar firma al PDF'.",
        )

    def on_acerca_de(self):
        QMessageBox.information(
            self,
            "Acerca de DocuSecure",
            "Aplicación de Firma Digital de Documentos\n"
            "Asignatura: Desarrollo de Interfaces (2º DAM)\n"
            "Tecnologías: PySide6 + pypdf",
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
