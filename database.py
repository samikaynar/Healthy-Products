import mysql.connector



# Connect to MySQL database

def get_connection():
    
    return  mysql.connector.connect(
        host="localhost",
        user="root",
        password="197e2161",
        database="healthy_products_db",
    )


