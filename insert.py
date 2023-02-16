import sqlite3
conn=sqlite3.connect('Mit mid morning.db')
print("open database successfully")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (1,'ERIC',30,'emoblis','male')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (2,'JOHN',25,'kamagut','Male')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (3,'ELSIE',19,'SEGERO','female')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (4,'IVY',18,'KAPENGURIA','female')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (5,'HESBON',29,'KENYA HIGH','MALE')")

conn.commit()
print("Records added successfull")
conn.close()
