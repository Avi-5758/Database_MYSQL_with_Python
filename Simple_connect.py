import mysql.connector

try:
    # Connect to the local MySQL server
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",  # Replace with your actual password
        database="my_database"
    )

    if db.is_connected():
        print("Connected successfully to MySQL database!")

except mysql.connector.Error as err:
    print(f"Failed to connect: {err}")

finally:
    # Close connection when finished
    if 'db' in locals() and db.is_connected():
        db.close()
        print("Connection closed.")