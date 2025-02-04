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
