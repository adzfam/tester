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
    age = random.randint(5, 20)
    address = fake.address()

    v[uuid.uuid1()] = {"firstname": f,
                       "lastname": l,
                       "age": age,
                       "date": timestampStr}

# prints with the key
# for x in v.items():
# print(x)

# prints without the key
for x in v:
    print(v[x])

# --------------------------------------------------------
print("----------")
# Code for Accounts and Transactions
for _ in range(10):
    accounts = {"firstname": f,
                "last name": l,
                "Balance": 100,
                }
    print(accounts)

# -----------------------------------------
class People:
    pass
Person1 = People()
Person2 = People()

Person1.first = f
Person1.last = l
Person1.age = age
Person1.address = address
Person1.Money = 100
#----------------
class People:
    def __init__(self, first, last, age, money):
        self.first = first
        self.last = last
        self.age = age
        self.money = money
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.):
            raise StopIteration



Person1 = People(f, l, age, 100)
Person2 = People()

print(People)
# #------------------------------------------
#
# #------------------------------------------
# # conn = sqlite3.connect('tester.db')
# # c = conn.cursor()
# # #create table
# # c.execute('''CREATE TABLE Tester
# #             (ID, first name, last name, age)''')
# # #insert row of data
# # c.execute("INSERT INTO Tester VALUES (v)")
# #
# #
# # #Save commit changes
# # conn.commit()
# #
# # #close after saving
# # c.close()
# # conn.close()
# #
# # for row in c.execute('SELECT * FROM Tester ORDER BY first name'):
# #         print(row)
# #
# # #------------------------------------------------
# #
# #
# # # columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in v.keys())
# # # values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in v.values())
# # # sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('mytable', columns, values)
# # # print(sql)
#
#
#
