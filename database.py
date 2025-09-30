import mysql.connector
import os
from dotenv import load_dotenv



# Connect to MySQL database

def get_connection():
    
    return  mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DATABASE_PASSWORD"),
        database="healthy_products_db",
    )


