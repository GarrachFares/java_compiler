import os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout
 
 
class UiMainWindow(QMainWindow):
    def __init__(self, MainWindow: QMainWindow):
        super(UiMainWindow, self).__init__()
        MainWindow.setFixedSize(900, 600)  # change the size of the main window
        self.MainWidget = QtWidgets.QWidget(MainWindow)
 
        self.MainWindow = MainWindow
 
        self.lineEdit = QtWidgets.QTextEdit(self.MainWidget)
        self.text_edit = QtWidgets.QTextEdit(self.MainWidget)
 
        self.setup_UI(MainWindow)
        self.setStyleSheets()
 
    def setup_UI(self, MainWindow: QMainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("My Personal Compiler")
        self.MainWidget.setObjectName("mainwidget")
        MainWindow.setCentralWidget(self.MainWidget)
 
        layout = QVBoxLayout(self.MainWidget)
 
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Place your code here...")
        self.lineEdit.setFont(QtGui.QFont('Arial', 12))
 
        self.startButton = QtWidgets.QPushButton(self.MainWidget)
        self.startButton.setObjectName("pushButton")
        self.startButton.setText("Compile")
        self.startButton.setFont(QtGui.QFont('Arial', 12))
 
        self.text_edit.setObjectName("scrollArea")
        self.text_edit.setReadOnly(True)
        self.text_edit.setPlaceholderText("Compilation result will appear here...")
        self.text_edit.setFont(QtGui.QFont('Arial', 12))
 
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.startButton)
        layout.addWidget(self.text_edit)
 
        self.startButton.clicked.connect(self.start)
 
    def start(self):
        with open("input.java", "w+") as input:
            input.write(self.lineEdit.toPlainText())
 
        os.system("compiler.exe < input.java 1>output.txt 2>error.txt")
        with open("output.txt", "r") as input_file:
            text = input_file.read()
            if text:
                self.text_edit.append("Compiled successfully ! \n")
                self.text_edit.append(text)
        with open("error.txt", "r") as error_file:
            text = error_file.read()
            if text:
                self.text_edit.append("Error !\n")
                self.text_edit.append(text)
 
    def setStyleSheets(self):
        self.MainWindow.setStyleSheet(".QPushButton {\n"
                                      "background-color: #FF6347; \n"
                                      "  color: white; \n"
                                      "  border: 2px solid #8B0000;\n"
                                      "  text-align: center;\n"
                                      "}\n"
                                      ".QTextEdit {\n"
                                      "background-color: #F5F5F5; \n"
                                      "  color: black; \n"
                                      "  border: 2px solid #A9A9A9;\n"
                                      "}\n"
                                      ".QWidget {\n"
                                      "background-color: #FFF8DC;\n"
                                      "}")
 