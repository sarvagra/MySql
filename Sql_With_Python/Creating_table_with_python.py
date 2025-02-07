import mysql.connector
from Sql_With_Python.credentials import DATABASE_CONFIG  

# Establish a connection
mydb = DATABASE_CONFIG

# Create a cursor object
mycursor = mydb.cursor()

# Execute a query to create a table
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS `table` (
        `Serial No` INT,
        `Name` VARCHAR(50),
        `Marks` FLOAT
    )
""")

# Close the cursor and connection
mycursor.close()
mydb.close()
