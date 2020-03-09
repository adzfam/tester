import random
import uuid
import names
from datetime import datetime
from faker import Faker

   
f = names.get_first_name()
l = names.get_last_name()
fake = Faker()
v = {}
dt = datetime.now()
timestampStr = dt.strftime("%d-%b-%Y")

##Code for user accounts--------------------------------
for _ in range(10):
 f = names.get_first_name()
 l = names.get_last_name()
 age = random.randint(5,20)
 address = fake.address()

 v[uuid.uuid1()] = {"firstname":f,
                    "lastname":l,
                    "age": age,
                    "address": address,
                    "date": timestampStr}

#prints with the key
#for x in v.items():
 #print(x)

#prints without the key
for x in v:
    print(v[x])

#--------------------------------------------------------
#Code for transactions & Money
transactions = {"firstname":f,
                "lastname":l,
                "balance": 100,
}


#-----------------------------------------
# conn = sqlite3.connect('tester.db')
# c = conn.cursor()
# #create table
# c.execute('''CREATE TABLE Tester
#             (ID, first name, last name, age)''')
# #insert row of data
# c.execute("INSERT INTO Tester VALUES (v)")
#
#
# #Save commit changes
# conn.commit()
#
# #close after saving
# c.close()
# conn.close()
#
# for row in c.execute('SELECT * FROM Tester ORDER BY first name'):
#         print(row)
#
# #------------------------------------------------
#
#
# # columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in v.keys())
# # values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in v.values())
# # sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('mytable', columns, values)
# # print(sql)



