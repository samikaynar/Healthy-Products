import sys
import mysql.connector
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from gui import HealthyProducts , QIcon
from create_username_gui import NewUserDialog 
from gui import HealthyProducts  
from user_page import User_Page


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="healthy_products_db",
)

cunn = mydb.cursor()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    stacked_widget=QStackedWidget()
    main_page=HealthyProducts(stacked_widget)
    new_user_page=NewUserDialog(stacked_widget)
    user_page=User_Page(stacked_widget)


    stacked_widget.addWidget(main_page)
    stacked_widget.addWidget(new_user_page)
    stacked_widget.addWidget(user_page)

    stacked_widget.setCurrentIndex(0)
    stacked_widget.setWindowIcon(QIcon("icon.png"))
    stacked_widget.setWindowTitle("Healthy Products Finder")
   


    stacked_widget.show()
    sys.exit(app.exec_())