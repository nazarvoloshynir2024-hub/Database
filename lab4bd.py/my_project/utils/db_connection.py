import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nazarbinance1",  # <--- ТВІЙ ПАРОЛЬ
            database="terminal_db"
        )
        return conn
    except Error as e:
        print(f"DB Error: {e}")
        return None