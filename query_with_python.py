import mysql.connector
from credentials import DATABASE_CONFIG  

# Establish a connection
mydb = DATABASE_CONFIG

# Create a cursor object
mycursor = mydb.cursor()

# Execute a query to create a table
mycursor.execute("SELECT * FROM test.table")
for i in mycursor.fetchall():
    print(i)             
# Close the cursor and connection
mycursor.close()
mydb.close()
