from random import random
import uuid
import names
import sqlite3
f = names.get_first_name()

l = names.get_last_name()
v = {}
for x in range(5):
 f = names.get_first_name()
 l = names.get_last_name()
 a = random()
# sada
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

#------------------------------------------------


# columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in v.keys())
# values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in v.values())
# sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('mytable', columns, values)
# print(sql)



#
#
#  )""")
#

# #print(l)
# #print(f, l)
# #----------------------
# dictionary = {
# 'First Name': f,
# 'Last Name': l,
# }
# print(dictionary)
# #------------------------
# dicts = {}
# keys = range(2)
# values = [f,l]
# for i in keys:
#  dicts[i] = values[i]
# print(dicts)
# # ------------------------
#
# o = dict(list(enumerate(values)))
# print(o)
# for keys in dicts:
#  print(keys)
# for values in dicts:
#  print(values)
# d = {'firstname': (f), 'last name': l}
# print(d)
