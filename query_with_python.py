import mysql.connector

# Establish a connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7334@Sql",
    database="test"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute a query to create a table
mycursor.execute("SELECT * FROM test.table")
for i in mycursor.fetchall():
    print(i)             
# Close the cursor and connection
mycursor.close()
mydb.close()
