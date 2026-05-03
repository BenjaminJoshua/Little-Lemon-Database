import mysql.connector as connector

# Connect to the database
try:
    connection = connector.connect(
        user="root", 
        password="your_password", # CHANGE THIS to your MySQL password
        host="127.0.0.1",
        database="LittleLemonDB"
    )
    print("Successfully connected to LittleLemonDB!")
    
    # Prove the connection works by calling GetMaxQuantity
    cursor = connection.cursor()
    cursor.callproc("GetMaxQuantity")
    
    for result in cursor.stored_results():
        print("Max Quantity in an order is:", result.fetchone()[0])

    connection.close()
except connector.Error as err:
    print(f"Error: {err}")
