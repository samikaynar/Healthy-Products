import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget,QLabel , QLineEdit ,QPushButton ,QVBoxLayout ,QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon , QFontDatabase , QIcon



class HealthyProducts(QWidget):
    def __init__(self,stacked_widget):
        super().__init__()
        self.stacked_widget=stacked_widget
        self.dash_label=QLabel("Welcome to the Healthy Products Finder App",self)
        self.dash_label2=QLabel("Enter your username\n(or create a new one if you don't have one)",self)
        self.input_user_name=QLineEdit(self)
        self.input_get=QPushButton("Submit Username",self)
        self.input_get_new_user_name=QPushButton("Create Unique Username",self)
        self.input_get_new_user_name.clicked.connect(self.go_to_new_user)
        self.test_button=QPushButton("check the user page",self)
        self.test_button.clicked.connect(self.go_to_user_page)

        self.initUI()

    def go_to_new_user(self):
        self.stacked_widget.setCurrentIndex(1)
    def go_to_user_page(self):
        self.stacked_widget.setCurrentIndex(2)


    def initUI(self):
        vbox=QVBoxLayout()
        vbox.addWidget(self.dash_label)
        vbox.addWidget(self.dash_label2)
        vbox.addWidget(self.input_user_name)
        vbox.addWidget(self.input_get)
        vbox.addWidget(self.input_get_new_user_name)
        vbox.addWidget(self.test_button)


        self.dash_label.setAlignment(Qt.AlignCenter)
        self.dash_label2.setAlignment(Qt.AlignCenter)
        self.input_user_name.setAlignment(Qt.AlignCenter)
        self.setLayout(vbox)

        
        self.dash_label.setObjectName("dash_label")
        self.dash_label2.setObjectName("dash_label2")
        self.input_user_name.setObjectName("input_user_name")
        self.input_get.setObjectName("input_get")
        self.input_get_new_user_name.setObjectName("input_get_new_user_name")

        self.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
                font-family: Arial, sans-serif;
                font-size: 14px;
            }
            QLabel#dash_label {
                font-size: 20px;
                font-weight: bold;
                color: #0d253f;
                margin-bottom: 15px;
            }
            QLabel#dash_label2 {
                font-size: 18px;      
                font-weight: 600;     
                color: #01b4e4;
                margin-bottom: 15px;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #01b4e4;
                color: white;
                padding: 8px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #90cea1;
            }
        """)

        

