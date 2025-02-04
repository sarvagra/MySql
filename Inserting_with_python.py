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
mycursor.execute("INSERT INTO test.table VALUES(01, 'Sarvagra', 90.00), (02, 'Gargi', 92.00)")
                
#commit so that the inserted data reflects in the table
mydb.commit()
# Close the cursor and connection
mycursor.close()
mydb.close()
