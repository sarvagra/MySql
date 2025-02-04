import mysql.connector
from credentials import DATABASE_CONFIG  

# Establish a connection
conn = DATABASE_CONFIG

# Create a cursor object
cursor = conn.cursor()

# Execute a query to create a database
cursor.execute("CREATE DATABASE IF NOT EXISTS test")

# Fetch all results to ensure there are no unread results
cursor.fetchall()

# Select the database
conn.database = "test"

# Execute another query after clearing the previous results
cursor.execute("SHOW DATABASES")

# Fetch all rows
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()