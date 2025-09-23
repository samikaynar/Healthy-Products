import sys
import mysql.connector
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from gui import HealthyProducts   
from create_username_gui import NewUserDialog 
from gui import HealthyProducts  


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
    database="healty_products_db",
)

cunn = mydb.cursor()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    stacked_widget=QStackedWidget()
    main_page=QStackedWidget(HealthyProducts)
    create_username_page=