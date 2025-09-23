import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget,QLabel , QLineEdit ,QPushButton ,QVBoxLayout ,QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon , QFontDatabase , QIcon

class NewUserDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.create_username_label=QLabel("Enter a Uniq Username",self)
        self.get_username=QLineEdit(self)
        self.check_username=QPushButton("Check your user name",self)
        self.initUI()

    def initUI(self):
        
