import mysql.connector as connector
import csv

connection = connector.connect(
    user="root", 
    password="your_password",
    host="127.0.0.1",
    database="LittleLemonDB"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM your_table")

# Write to CSV
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([i[0] for i in cursor.description])  # Write headers
    writer.writerows(cursor.fetchall())

connection.close()
