-- creating a database , always use  if not exists  to eliminate errors
CREATE DATABASE IF NOT EXISTS college; 
USE college;
CREATE TABLE student(
    rollno INT PRIMARY KEY ,
    name VARCHAR(50) UNIQUE, -- takes only unique name entries
    marks INT NOT NULL, -- means the column cant hold null value,
    grade VARCHAR(1) DEFAULT 'S', -- sets default value as S
    city VARCHAR(25)
);
INSERT INTO student(rollno, name, marks, grade, city)
VALUES
(100, "anil", 78, "C", "Pune"),
(101, "Gauri", 78, "C", "jaipur"),
(102, "bhumika", 93, "A", "Mumbai"),
(103, "chetan", 85, "B", "Mumbai"),
(104, "dhruv", 96, "A", "Delhi"),
(105, "emanuel", 12, "F", "Delhi"),
(106, "farah", 82, "B", "Delhi");

SELECT * FROM student;
SELECT name,marks FROM student;
SELECT DISTINCT city FROM student;
SELECT name,marks FROM student WHERE marks>80;
SELECT * FROM student
ORDER BY marks ASC;
SELECT * FROM student 
ORDER BY marks DESC
LIMIT 3;



-- Updating
UPDATE student
SET grade ="A"
WHERE 

-- Deleting
DELETE FROM student
WHERE grade="F"

-- ordering data
SELECT * FROM student
ORDER BY name DESC; -- DESC , ASC can be used to determine the order


SELECT * FROM student
ORDER BY marks,grade; -- first order by marks and then by grade

SELECT * FROM student
ORDER BY marks DESC
LIMIT 3;  -- find the top 3 students

-- filtering WHERE and IN keywords 
 SELECT * FROM student
 WHERE marks>80;

 SELECT * FROM student
 WHERE name IN ('chetan','gauri','anil')  -- note that it is not case sensitive

