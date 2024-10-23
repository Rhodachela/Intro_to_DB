import mysql.connector
from mysql.connector import errorcode

# Function to create the database
def create_database():
    cursor = None
    connection = None

    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',         # Change if needed
            user='root',              # Your MySQL username
            password='MySQL.Installer'   # Your MySQL password
        )
        
        # Create a cursor object
        cursor = connection.cursor()
        
        # SQL command to create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
        
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        # Close the cursor and connection
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

# Call the function to create the database
create_database()
