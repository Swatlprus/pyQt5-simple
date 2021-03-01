import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os.path


from requests import post
import json
import argparse
import base64
import re
import os
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger


class Form(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.plainTextEdit = QPlainTextEdit()
        self.plainTextEdit.setFont(QFont('Arial', 11))

        openDirButton = QPushButton("Выбрать каталог:")
        openDirButton.clicked.connect(self.getDirectory)

        openFileButton = QPushButton("Выбрать файл:")
        openFileButton.clicked.connect(self.getFilename)

        startButton = QPushButton("Запустить")
        startButton.clicked.connect(self.startSlice)

        layoutV = QVBoxLayout()
        layoutV.addWidget(openDirButton)
        layoutV.addWidget(openFileButton)
        layoutV.addWidget(startButton)

        layoutH = QHBoxLayout()
        layoutH.addLayout(layoutV)
        layoutH.addWidget(self.plainTextEdit)

        centerWidget = QWidget()
        centerWidget.setLayout(layoutH)
        self.setCentralWidget(centerWidget)

        self.resize(600, 50)
        self.setWindowTitle("Разделение PDF-документа")

    def getDirectory(self):
        global dirlist
        dirlist = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        self.plainTextEdit.appendHtml("Каталог: <b>{}</b>".format(dirlist))

    def getFilename(self):
        global filename
        filename, filetype = QFileDialog.getOpenFileName(self, "Выбрать файл", ".")
        self.plainTextEdit.appendHtml("Файл: <b>{}</b>".format(filename, filetype))

    def startSlice(self):
        # Модуль по разделению PDF на страницы - ЧАСТЬ 1
        pdf_document = filename
        pdf = PdfFileReader(pdf_document)
        for page in range(pdf.getNumPages()):
            pdf_writer = PdfFileWriter()
            current_page = pdf.getPage(page)
            pdf_writer.addPage(current_page)
            print(os.path.exists(dirlist + '/Slice'))
            outputFilename = "C:/Users/Ринат/PycharmProjects/pdfSlice/Slice/Slice-page-{}.pdf".format(page + 1)
            with open(outputFilename, "wb") as out:
                pdf_writer.write(out)
                print("created", outputFilename)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())