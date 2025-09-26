import sys
import mysql.connector
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from gui import HealthyProducts, QIcon
from create_username_gui import NewUserDialog
from gui import HealthyProducts  
from user_page import User_Page
from favorites_page import FavoritePage


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create a stacked widget to hold multiple pages
    stacked_widget = QStackedWidget()

    # Create each page and pass the stacked widget
    main_page = HealthyProducts(stacked_widget)   # Main Page: username input
    new_user_page = NewUserDialog(stacked_widget) # New User Page: create username
    user_page = User_Page(stacked_widget)         # User Page: search products
    favorites_page = FavoritePage(stacked_widget) # Favorites Page: view favorites

    # Add pages to the stacked widget
    stacked_widget.addWidget(main_page)
    stacked_widget.addWidget(new_user_page)
    stacked_widget.addWidget(user_page)
    stacked_widget.addWidget(favorites_page) 

    # Set the first page to show
    stacked_widget.setCurrentIndex(0)

    # Set window icon and title
    stacked_widget.setWindowIcon(QIcon("icon.png"))
    stacked_widget.setWindowTitle("Healthy Products Finder")

    # Show the window
    stacked_widget.show()

    # Start the application
    sys.exit(app.exec_())
