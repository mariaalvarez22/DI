import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from nortempi import Ui_MainWindow
from PySide6.QtWidgets import QToolBar
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QCursor


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.toolBar.setIconSize(QSize(64,64))

        # Cargar la imagen del cursor
        pixmap = QPixmap(r"C:\Users\HP\Desktop\2º DAM\DESARROLLO DE INTERFACES\Nortempito\IconoRaton1.png")
        pixmap = pixmap.scaled(72, 42, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

        # Aplicar como cursor
        self.setCursor(QCursor(pixmap))


        # Conectar botones
        self.act_Informacion.triggered.connect(self.mostrar_informacion)
        self.actionVolver_al_Inicio.triggered.connect(self.volver_inicio)
        self.actionSalir.triggered.connect(self.close)
        self.action_Contacto.triggered.connect(self.mostrar_contacto)


        # QLabel de fondo principal
        self.fondo_label = QLabel(self.centralwidget)
        self.fondo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fondo_label.lower()
        self.fondo_pixmap = QPixmap("nortempi.jpg")

        # QLabel de fondo para contacto
        self.contacto_fondo_label = QLabel(self.centralwidget)
        self.contacto_fondo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.contacto_fondo_label.lower()
        self.contacto_pixmap = QPixmap("contacto.jpg")
        self.contacto_fondo_label.hide()

        # Labels de información
        self.label_width = 350
        self.label_height = 500
        self.margin = 20

        self.label_dam = QLabel(self.centralwidget)
        self.label_dam.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.label_dam.setWordWrap(True)
        self.label_dam.setStyleSheet("""
            background-color: rgba(255, 255, 255, 200);
            border: 2px solid gray;
            border-radius: 10px;
            padding: 15px;
            color: black;
            font-size: 14px;
        """)
        self.label_dam.hide()

        self.label_daw = QLabel(self.centralwidget)
        self.label_daw.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.label_daw.setWordWrap(True)
        self.label_daw.setStyleSheet("""
            background-color: rgba(255, 255, 255, 200);
            border: 2px solid gray;
            border-radius: 10px;
            padding: 15px;
            color: black;
            font-size: 14px;
        """)
        self.label_daw.hide()

        # Mostrar fondo inicial
        self.actualizar_fondo_principal()

    def actualizar_fondo_principal(self):
        pixmap_ajustado = self.fondo_pixmap.scaled(
            self.centralwidget.width(),
            self.centralwidget.height(),
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
        )
        self.fondo_label.setPixmap(pixmap_ajustado)
        self.fondo_label.setGeometry(0, 0, self.centralwidget.width(), self.centralwidget.height())
        self.fondo_label.show()
        self.contacto_fondo_label.hide()

    def actualizar_fondo_contacto(self):
        pixmap_ajustado = self.contacto_pixmap.scaled(
            self.centralwidget.width(),
            self.centralwidget.height(),
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
        )
        self.contacto_fondo_label.setPixmap(pixmap_ajustado)
        self.contacto_fondo_label.setGeometry(0, 0, self.centralwidget.width(), self.centralwidget.height())
        self.contacto_fondo_label.show()
        self.fondo_label.hide()

    def volver_inicio(self):
        self.label_dam.hide()
        self.label_daw.hide()
        self.actualizar_fondo_principal()
        self.statusbar.showMessage("Se ha vuelto al inicio", 5000)


#SACAR POR PANTALLA LA INFORMACIONSSSSS
    def mostrar_informacion(self):
        texto_dam = (
        "<h2 style='color:#1E90FF;'>DAM – Desarrollo de Aplicaciones Multiplataforma</h2>"
        "<p><b>Duración total:</b> 2.000 horas</p>"
        "<p><b>Modalidad:</b> Presencial (€4.000) / Online (€3.000)</p>"
        "<p><b>Inicio de curso:</b> Septiembre 2026</p>"
        "<p><b>Objetivo:</b> Formar profesionales capaces de desarrollar aplicaciones para diferentes plataformas "
        "y entornos, tanto de escritorio como móviles.</p>"
        "<p><b>Contenidos principales:</b></p>"
        "<ul>"
        "<li>Programación en Java y Kotlin</li>"
        "<li>Desarrollo de interfaces gráficas</li>"
        "<li>Acceso a bases de datos y servicios web</li>"
        "<li>Gestión de proyectos de software</li>"
        "<li>Diseño de aplicaciones móviles</li>"
        "<li>Depuración de software</li>"
        "<li>Control de versiones con Git</li>"
        "<li>Buenas prácticas de desarrollo y metodologías ágiles</li>"
        "</ul>"
    )

        texto_daw = (
        "<h2 style='color:#32CD32;'>DAW – Desarrollo de Aplicaciones Web</h2>"
        "<p><b>Duración total:</b> 2.000 horas</p>"
        "<p><b>Modalidad:</b> Presencial (€4.000) / Online (€3.000)</p>"
        "<p><b>Inicio de curso:</b> Septiembre 2026</p>"
        "<p><b>Objetivo:</b> Formar profesionales especializados en el desarrollo de aplicaciones y servicios web, "
        "front-end y back-end.</p>"
        "<p><b>Contenidos principales:</b></p>"
        "<ul>"
        "<li>HTML, CSS, JavaScript y frameworks modernos</li>"
        "<li>Desarrollo de APIs y bases de datos</li>"
        "<li>Gestión de servidores y despliegue web</li>"
        "<li>Seguridad y buenas prácticas de desarrollo</li>"
        "<li>Diseño responsive y accesibilidad</li>"
        "<li>Optimización y rendimiento web</li>"
        "<li>Integración de servicios en la nube</li>"
        "<li>Metodologías ágiles y gestión de proyectos web</li>"
        "</ul>"
    )

        self.label_dam.setText(texto_dam)
        self.label_daw.setText(texto_daw)
        self.label_dam.show()
        self.label_daw.show()
        self.fondo_label.show()
        self.contacto_fondo_label.hide()
        self.statusbar.showMessage("Se ha pulsado el botón de información", 5000)

    def mostrar_contacto(self):
        self.label_dam.hide()
        self.label_daw.hide()
        self.actualizar_fondo_contacto()
        self.statusbar.showMessage("Se ha pulsado el botón de contacto", 5000)

    def resizeEvent(self, event):
        # Ajustar fondo y labels al redimensionar

        self.actualizar_fondo_principal()
        label_width = int(self.width() * 0.35)   # ancho relativo
        label_height = int(self.height() * 0.7)  # alto relativo
        espacio_entre_labels = 20 # 5% del ancho como separación
    
        total_width = label_width * 2 + espacio_entre_labels
        inicio_x = (self.width() - total_width) // 2
        y = 50
        self.label_dam.setGeometry(inicio_x, y, label_width, label_height)
        self.label_daw.setGeometry(inicio_x + label_width + espacio_entre_labels, y, label_width, label_height)
        if self.contacto_fondo_label.isVisible():
            self.actualizar_fondo_contacto()
        super().resizeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())