import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import create_user_service

class NewUserDialog(QWidget):
    def __init__(self,stacked_widget):
        super().__init__()
        self.stacked_widget=stacked_widget
        self.create_username_label = QLabel("Enter a Unique Username and password", self)
        self.get_username = QLineEdit(self)
        self.get_password = QLineEdit(self)
        self.check_username = QPushButton("Check Username", self)
        self.result_label = QLabel(self)
        self.main_page=QPushButton("Main Page",self)
        self.main_page.clicked.connect(self.go_to_main_page)
        self.check_username.clicked.connect(self.create_user_button)
        self.initUI()
    
    def go_to_main_page(self):
        self.stacked_widget.setCurrentIndex(0)

    def initUI(self):
        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.create_username_label)
        vbox.addWidget(self.get_username)
        vbox.addWidget(self.get_password)
        vbox.addWidget(self.result_label)
        vbox.addWidget(self.check_username)
        vbox.addWidget(self.main_page)
        self.setLayout(vbox)

        # Alignment
        self.create_username_label.setAlignment(Qt.AlignCenter)
        self.get_username.setAlignment(Qt.AlignCenter)
        self.get_password.setAlignment(Qt.AlignCenter)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.check_username.setAutoDefault(True)

        # Object names for styling
        self.create_username_label.setObjectName("create_username_label")
        self.get_username.setObjectName("get_username")
        self.check_username.setObjectName("check_username")
        self.main_page.setObjectName("main_page")

        # Stylesheet
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
                font-family: Arial, sans-serif;
                font-size: 14px;
            }
            QLabel#create_username_label {
                font-size: 18px;
                font-weight: bold;
                color: #0d253f;
                margin-bottom: 15px;
            }
            QLineEdit#get_username {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 14px;
                margin-bottom: 10px;
            }
            QPushButton#check_username {
                background-color: #01b4e4;
                color: white;
                padding: 8px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton#check_username:hover {
                background-color: #90cea1;
            }
            QPushButton#main_page {
                background-color: #01b4e4;
                color: white;
                padding: 8px;
                border-radius: 5px;
                font-weight: bold;
            }

            QPushButton#main_page:hover {
                background-color: #90cea1;
                
                    }
                           

        """)

    
    def create_user_button(self):
        username = self.get_username.text()
        password = self.get_password.text()

        if create_user_service.create_user(username,password):
            self.result_label.setText("Success! User created successfully!")
            self.result_label.setStyleSheet("color: green; font-weight: bold; font-size: 15px")
            self.result_label.setFixedSize(300, 30)
        else:
            self.result_label.setText("Error! Username already exists!")
            self.result_label.setStyleSheet("color: red; font-weight: bold; font-size: 15px")
            self.result_label.setFixedSize(300, 30)

