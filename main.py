import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Form(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.plainTextEdit = QPlainTextEdit()
        self.plainTextEdit.setFont(QFont('Arial', 11))

        openDirButton = QPushButton("Открыть каталог:")
        openDirButton.clicked.connect(self.getDirectory)

        startButton = QPushButton("Запустить")
        startButton.clicked.connect(self.getDirectory)

        layoutV = QVBoxLayout()
        layoutV.addWidget(openDirButton)
        layoutV.addWidget(startButton)

        layoutH = QHBoxLayout()
        layoutH.addLayout(layoutV)
        layoutH.addWidget(self.plainTextEdit)

        centerWidget = QWidget()
        centerWidget.setLayout(layoutH)
        self.setCentralWidget(centerWidget)

        self.resize(600, 50)
        self.setWindowTitle("Разделение PDF-документа")

    def getDirectory(self):  # <-----
        dirlist = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        self.plainTextEdit.appendHtml("<br><b>{}</b>".format(dirlist))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())