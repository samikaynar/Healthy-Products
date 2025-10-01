import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTableWidget, QHBoxLayout , QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from database import get_connection



class FavoritePage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.back_button = QPushButton("Back to User Page", self)
        self.delete_button = QPushButton("Delete Selected", self)
        self.personality_label = QLabel("AI Doctor: Here will be your health advice...", self)
        self.doctor_picture=QLabel(self)
        self.pixmap=QPixmap("snakedoctor.png")
        self.table=QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Product Name", "Product Barcode", "Healty Score"])



        
        self.back_button.clicked.connect(self.go_back)
        
        self.initUI()
        

    def showEvent(self, event):
        self.current_user_id = self.stacked_widget.current_user_id 
        self.display_favorites()
        super().showEvent(event)
        
    #connection for user page
    def go_back(self):
        self.stacked_widget.setCurrentIndex(2)

    def display_favorites(self):

        
        self.current_user_id=self.stacked_widget.current_user_id
        db=get_connection()
        curr=db.cursor()
        curr.execute(""" select 
                        products.name,
                        products.barcode,
                        ai_analysis.health_score
                        from favorites
                        join products on favorites.product_id = products.id
                        left join ai_analysis on products.id = ai_analysis.product_id
                        where favorites.user_id = %s
                      """,(self.current_user_id,))
        
        results=curr.fetchall()
        
        self.table.setRowCount(len(results))


        for index,data in enumerate(results):
            self.table.setItem(index,0,QTableWidgetItem(str(data[0])))
            self.table.setItem(index,1,QTableWidgetItem(str(data[1])))
            self.table.setItem(index,2,QTableWidgetItem(str(data[2])))
        
        self.table.show()
        


    #Interface
    def initUI(self):
      
      #doctor picture
      scaled_pixmap = self.pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
      self.doctor_picture.setPixmap(scaled_pixmap)
      #table
      self.table=QTableWidget()
      self.table.setColumnCount(2)
      self.table.setHorizontalHeaderLabels(["Product Name","Health Score(1-10)"])
      self.table.setMinimumHeight(200)
      

      vbox=QVBoxLayout()
      button_bar=QHBoxLayout()
      button_bar.addWidget(self.back_button)
      button_bar.addWidget(self.delete_button)
      button_bar.addStretch()


      doctor_layout=QHBoxLayout()
      doctor_layout.addWidget(self.doctor_picture)
      doctor_layout.addWidget(self.personality_label)
      doctor_layout.addStretch()
      

      vbox.addWidget(self.table)
      vbox.addLayout(button_bar)
      vbox.addLayout(doctor_layout)
      self.setLayout(vbox)



      self.back_button.setObjectName("back_button")
      self.delete_button.setObjectName("delete_button")
      self.table.setObjectName("favorites_table")
      self.personality_label.setObjectName("personality_label")
      self.doctor_picture.setObjectName("doctor_picture")
      
       # Stylesheet
      self.setStyleSheet("""
            /* Whole page background and text */
            QWidget {
                background-color: #f5f5f5;
                font-family: Arial, sans-serif;
                font-size: 14px;
                color: #0d253f;
            }

            /* Buttons */
            QPushButton {
                background-color: #01b4e4;
                color: white;
                padding: 8px 12px;
                border-radius: 8px;
                border: none;
                font-weight: bold;
                min-height: 34px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #0193c6;
            }

            QPushButton#back_button {
                background-color: #f05454;
            }
            QPushButton#back_button:hover {
                background-color: #e64545;
            }

            QPushButton#delete_button {
                background-color: #ff7675;
            }
            QPushButton#delete_button:hover {
                background-color: #ff5958;
            }

            /* Table look */
            QTableWidget#favorites_table {
                background-color: #ffffff;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
            }
            QTableWidget#favorites_table QHeaderView::section {
                background-color: #01b4e4;
                color: white;
                font-weight: bold;
                padding: 5px;
                height: 20px;
                border: none;
            }
            QTableWidget#favorites_table::item {
                background-color: #fdfdfd;
                color: #0d253f;
                padding: 6px;
                border-bottom: 1px solid #e0e0e0;
            }
            QTableWidget::item:selected {
                background-color: #90cea1;
                color: #0d253f;
            }

            /* Doctor picture */
            QLabel#doctor_picture {
                border-radius: 10px;
                padding: 2px;
                background-color: transparent;
            }

            /* AI text */
            QLabel#personality_label {
                font-size: 15px;
                color: #0d253f;
                padding-left: 10px;
            }
            """)




    