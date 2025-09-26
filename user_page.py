import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel , QLineEdit ,QPushButton ,QVBoxLayout ,QMainWindow , QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon , QFontDatabase , QIcon



class User_Page(QWidget):
    def __init__(self,stacked_widget):
        super().__init__()
        self.stacked_widget=stacked_widget
        self.log_out_label=QPushButton("Log out",self)
        self.label1=QLabel("Inser the product name or\nbarcode to check",self)
        self.input_product=QLineEdit(self)
        self.get_input_button=QPushButton("Check",self)
        self.result_label=QLabel(self)
        self.AI_label=QLabel(self)
        self.get_favorite=QPushButton("View Favorites",self)
        self.log_out_label.clicked.connect(self.log_out_button)
        self.get_favorite.clicked.connect(self.go_to_favorites)
        self.initUI()


    def log_out_button(self):
        self.stacked_widget.setCurrentIndex(0)
    
    def go_to_favorites(self):
        self.stacked_widget.setCurrentIndex(3)

    def initUI(self):
        vbox=QVBoxLayout()
        top_bar=QHBoxLayout()

        top_bar.addWidget(self.log_out_label)
        top_bar.addStretch()                   
        vbox.addLayout(top_bar)

        
        vbox.addWidget(self.label1)
        vbox.addWidget(self.input_product)

        hbox=QHBoxLayout()
        hbox.addWidget(self.get_input_button)
        hbox.addWidget(self.get_favorite)
        vbox.addLayout(hbox)



        vbox.addWidget(self.result_label)
        vbox.addWidget(self.AI_label)
        
        self.setLayout(vbox)
        self.label1.setAlignment(Qt.AlignCenter)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.AI_label.setAlignment(Qt.AlignCenter)

        
        self.label1.setObjectName("label1")
        self.result_label.setObjectName("result_label")
        self.AI_label.setObjectName("AI_label")
        self.log_out_label.setObjectName("log_out_label")

        self.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
                font-family: Arial, sans-serif;
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
            
            QPushButton#log_out_label {
                background-color: #f05454;
                color: white;
                padding: 6px 12px;
                font-weight: bold;
            }
            
            QPushButton#log_out_label:hover {
                background-color: #ff7675;
            }
            
            QLabel {
                color: #0d253f;
            }
            
            QLabel#label1 {
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            
            QLabel#result_label {
                font-size: 16px;
                color: #01b4e4;
                margin-top: 15px;
                min-height: 30px;
            }
            
            QLabel#AI_label {
                font-size: 16px;
                color: #0d253f;
                margin-top: 10px;
                min-height: 30px;
            }
            
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 14px;
                margin-bottom: 10px;
            }
        """)


        
        

