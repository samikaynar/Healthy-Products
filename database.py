import mysql.connector



# Connect to MySQL database

def get_connection():
    
    return  mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="healthy_products_db",
    )


