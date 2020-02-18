from random import random
import uuid
import names
import sqlite3
f = names.get_first_name()
#print(f)
l = names.get_last_name()
v = {}
for x in range(5):
 f = names.get_first_name()
 l = names.get_last_name()
 a = random()

 v[uuid.uuid1()] = {"firstname":f, "lastname":l,"age": a}
#print(v)
#-----------------------------------------
conn = sqlite3.connect('tester.db')
c = conn.cursor()
#create table
c.execute('''CREATE TABLE Tester
            (ID, first name, last name, age)''')
#insert row of data
c.execute("INSERT INTO Tester VALUES (v)")


#Save commit changes
conn.commit()

#close after saving
c.close()
conn.close()

for row in c.execute('SELECT * FROM Tester ORDER BY first name'):
        print(row)
