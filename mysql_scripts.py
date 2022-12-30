import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dantala@001",
    database="dan_database"
)

mycursor=db.cursor()
#mycursor.execute("CREATE DATABASE dan_database")
#mycursor.execute("CREATE TABLE students(name VARCHAR(45), age smallint UNSIGNED, class VARCHAR(28), personID int PRIMARY KEY AUTO_INCREMENT)")
# to see details on the executed table above 
#mycursor.execute("INSERT INTO students (name, age, class) VALUES (%s,%s,%s)", ("james", 15, "ss1"))
#mycursor.execute("INSERT INTO students (name, age, class) VALUES (%s,%s,%s)", ("lily", 14, "ss2"))
#db.commit()

mycursor.execute("SELECT * FROM students")
for i in mycursor:
    print(i)