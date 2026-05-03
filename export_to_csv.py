import mysql.connector as connector
import csv

# Connect to the database
try:
    connection = connector.connect(
        user="root", 
        password="your_password",  # CHANGE THIS to your MySQL password
        host="127.0.0.1",
        database="LittleLemonDB"
    )
    print("Successfully connected to LittleLemonDB!")
    
    cursor = connection.cursor()
    
    # Define tables and their output files
    tables = ['Customers', 'Bookings', 'Orders']
    
    for table in tables:
        # Fetch all data from the table
        cursor.execute(f"SELECT * FROM {table}")
        
        # Get column names
        columns = [i[0] for i in cursor.description]
        
        # Get all rows
        rows = cursor.fetchall()
        
        # Write to CSV file
        filename = f"{table}.csv"
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(columns)  # Write headers
            writer.writerows(rows)    # Write data rows
        
        print(f"✓ Exported {filename} ({len(rows)} rows)")
    
    connection.close()
    print("\nAll CSV files created successfully for Tableau!")
    
except connector.Error as err:
    print(f"Error: {err}")