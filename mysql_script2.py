import mysql.connector
from datetime import datetime

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dantala@001",
    database="dan_database"
)


mycursor=db.cursor()
#create table
#mycursor.execute("CREATE TABLE stocks(name VARCHAR(50) NOT NULL, price int NOT NULL , sector ENUM('IT','Manufacturing','Health') NOT NULL, created datetime NOT NULL, Stock_id int PRIMARY KEY AUTO_INCREMENT )")
#db.commit()

# insert data into table
#mycursor.execute("INSERT INTO stocks(name, price, sector, created) VALUES (%s,%s,%s,%s)",("Biocon", 50, "Health", datetime.now()))
#db.commit()

# extract from table
#mycursor.execute("SELECT price FROM stocks WHERE sector = 'IT' ORDER BY Stock_id DESC")
#mycursor.execute("SELECT * FROM stocks ORDER BY Stock_id DESC")
#mycursor.execute("SELECT price, name FROM stocks WHERE sector = 'IT' ORDER BY Stock_id DESC")

# modify table
#mycursor.execute("ALTER TABLE stocks ADD COLUMN Year_founded int NOT NULL")
#mycursor.execute("INSERT INTO stocks(name, price, sector, created, Year_founded) VALUES (%s,%s,%s,%s,%s)",("Biocon", 50, "Health", datetime.now(), 1978))
#db.commit()

# delete column from the table
#mycursor.execute("ALTER TABLE stocks DROP Year_founded ")

# change name of a current column in the table 
#mycursor.execute("ALTER TABLE stocks CHANGE name Company_name VARCHAR(50)")


# describe columns in the table
mycursor.execute("DESCRIBE stocks")

for a in mycursor:
    print(a)
    



