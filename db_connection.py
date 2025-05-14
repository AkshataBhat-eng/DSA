import mysql.connector
from mysql.connector import Error



def fetch_users():
    connection = mysql.connector.connect(
            host='localhost',
            user='appuser',
            password='Akshata123##',
            database='userDB'
        )
    try: 
        
        if connection.is_connected():
            print("Connected to database")
            cursor = connection.cursor()
            query = "SELECT * from users;"
            cursor.execute(query)

            results = cursor.fetchall()

            print("Users table")
            for row in results:
                print(f"ID: {row[0]}, Name: {row[1]}, Place: {row[2]}, Phone Number: {row[3]}")
    
    except Error as e:
        print("Error in connection: ",e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")


fetch_users()