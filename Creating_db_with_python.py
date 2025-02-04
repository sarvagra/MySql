import mysql.connector

# Establish a connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7334@Sql"
)

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
