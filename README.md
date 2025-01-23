# MySql
Contains all self made notes for Sql

# Keys
**Primary Key:**
It is a column or a set of columns in a table that uniquely identifies each row. There is only one PK ans it cant be null.
Primary keys can be assigned in two ways:
1) CREATE TABLE table(
    id INT,
    name VARCHAR,
    age INT,
    PRIMARY KEY(id,....(can add others too to make combined PKs))  //remember that combination will be unique not individual column elements in case of a multiple declaration.
    )
2) CREATE TABLE table(
    id INT PRIMARY KEY,
    name VARCHAR,
    age INT
    )

**Foreign Key:**
It is a column or a set of columns in a table that refers to the primery key in another table. There can be multiple FKs and can have duplicate values and null values.
Declaration:

CREATE TABLE temp(
    id INT,
    FOREIGN KEY(id)//new table// refrences costumer(cust_id)//old //table
)

# Constraints:
**Not Null:**
Columns cannot have null values.

**Unique:**
All values in a column are unique.

**Primary Key:**
Makes a column unique and not null (only for one column). 

**Default:**
sets the default value of a column 
>> salary INT DEFAULT 25000

**Check:**
It can limit the values allowed in a column
>> CONSTRAINT age_check CHECK(age>=18 AND city="Delhi") , OR->
>> age INT CHECK(age>=18)

# Select in detail
**Basic syntax:**
SELECT COL1,COL2 FROM table_name;

**To select all:**
SELECT * FROM table_name;

note : TO REMOVE DUPLICATES FROM A COLUMN WHEN PRINTING IT, WE CAN USE "DISTINCT" KEYWORD
SELECT DISTINCT city from student;

**WHERE clause:**
Used to define conditions whether to print an element or not.
Syntax:
SELECT col1, col2 FROM table_ name
WHERE conditions;

Example:
SELECT * FROM student WHERE marks > 80; //'>' can be replaced by logical, arithematical and conditional operators i.e. +, -, /, %, =, !=, <, <=, >=, AND, OR, NOT, IN, BETWEEN, ALL, LIKE, ANY, bitwise &, bitwise |//
SELECT * FROM student WHERE city = "Mumbai";

**LIMIT clause:**
sets an upper limit on the number of rows(tuples) to be printed.For example:
SELECT * FROM student LIMIT 3;

**ORDER BY clause:**
To sort in ascending(ASC) or descending order(DESC).Syntax:
SELECT * FROM student
ORDER BY marks ASC;

# Aggregate Functions
