from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QCoreApplication

from object_identifier import ObjectIdentifier

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Recognito")
        self.setMinimumSize(500, 400)

        self.label_file = QLabel("Enter a file:", self)
        self.label_file.move(10, 10)

        self.entry_file = QLineEdit(self)
        self.entry_file.setGeometry(100, 10, 300, 25)

        self.button_browse = QPushButton("Browse", self)
        self.button_browse.setGeometry(410, 10, 80, 25)
        self.button_browse.clicked.connect(self.browse_file)

        self.button_identify = QPushButton("Identify", self)
        self.button_identify.setGeometry(210, 50, 80, 30)
        self.button_identify.clicked.connect(self.identify_file)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setGeometry(10, 100, 480, 400)

        self.filepath_label = QLabel(self)
        self.filepath_label.setAlignment(Qt.AlignCenter)
        self.filepath_label.setGeometry(10, 510, 480, 25)

        self.center_window()

    def browse_file(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Select a file", "", "Image files (*.jpg *.jpeg *.png);;All files (*.*)")
        if filepath:
            image = QImage(filepath)
            if image.width() < image.height() or image.width() == image.height():
                self.entry_file.setText(filepath)
                self.render_image(filepath)
                self.center_window()
            else:
                QMessageBox.warning(self, "Invalid Image", "Please select an image with width less than height.")

    def identify_file(self):
        filepath = self.entry_file.text()
        if filepath == "":
            QMessageBox.critical(self, "Error", "Please browse a file first.")
            return

        obj_id = ObjectIdentifier()
        self.filepath_label.setText(obj_id.run_object_detection(filepath))

    def render_image(self, filepath):
        image = QImage(filepath)

        scaled_image = image.scaled(self.image_label.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
        pixmap = QPixmap.fromImage(scaled_image)

        self.image_label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height() + 200)
        self.center_window()

    def center_window(self):
        frame_geo = self.frameGeometry()
        screen = QCoreApplication.instance().desktop().screenGeometry()
        center_point = screen.center()
        frame_geo.moveCenter(center_point)
        self.move(frame_geo.topLeft())

    def resizeEvent(self, event):
        super().resizeEvent(event)

        if self.image_label.pixmap() is not None:
            self.render_image(self.entry_file.text())
