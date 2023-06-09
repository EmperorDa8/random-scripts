import mysql.connector
from datetime import datetime

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dantala@001",
    database= "school_db"
)


teacher_s=[("joy", "grace", 30, "Male", datetime.now()),
           ("fred", "ahmed", 27, "Male", datetime.now()),
           ("vivian", "tunde", 29, "Female", datetime.now())]


grades=[( "class 1c", 30, "english lang", 1),
        ( "class 1d", 20, "mathematics", 2),
        ( "class 2c", 22, "civil education", 3)]




mycursor=db.cursor()


#G1= 'CREATE DATABASE school_db'
G2= 'CREATE TABLE teachers(first_name VARCHAR(20) NOT NULL, last_name VARCHAR(25) NOT NULL, age int NOT NULL, gender ENUM("Male","Female") NOT NULL, created datetime NOT NULL, Id int PRIMARY KEY AUTO_INCREMENT )'
G1='CREATE TABLE Grades(class VARCHAR(20) NOT NULL, class_size int NOT NULL, subject VARCHAR(30) NOT NULL, T_Id int PRIMARY KEY, FOREIGN KEY(T_Id) REFERENCES teachers(Id))'
G3="INSERT INTO teachers (first_name, last_name, age, gender, created) VALUES (%s, %s, %s, %s, %s)"
G4="INSERT INTO Grades (class, class_size, subject, T_Id) VALUES (%s, %s, %s, %s)"
D1= "DROP TABLE Grades"
D2= "DROP TABLE teachers"
#mycursor.executemany(G3, teacher_s)
#mycursor.executemany(G4, grades)
#mycursor.execute()
#for i in mycursor:
#   print(i)
#db.commit()