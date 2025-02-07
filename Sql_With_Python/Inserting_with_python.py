import mysql.connector
from Sql_With_Python.credentials import DATABASE_CONFIG  

# Establish a connection
mydb = DATABASE_CONFIG

# Create a cursor object
mycursor = mydb.cursor()

# Execute a query to create a table
mycursor.execute("INSERT INTO test.table VALUES(01, 'Sarvagra', 90.00), (02, 'Gargi', 92.00)")
                
#commit so that the inserted data reflects in the table
mydb.commit()
# Close the cursor and connection
mycursor.close()
mydb.close()
