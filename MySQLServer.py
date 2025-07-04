import mysql.connector

def create_database():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # replace with your MySQL root password if needed
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
