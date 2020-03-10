import random
import uuid
import names
from datetime import datetime
from faker import Faker

fake = Faker()
v = {}
dt = datetime.now()
timestampStr = dt.strftime("%d-%b-%Y")
# ----------------------------------------
# List containing all the users
keys = ["ID", "first name", "last name", "age", "time"]
# Creating the Dict with UUID
for _ in range(5):
    f = names.get_first_name()
    l = names.get_last_name()
    age = random.randint(9, 50)
    t = timestampStr
    id = uuid.uuid1()
    users = [id, f, l, age, t]
    new = {}
    for i in range(5):
        new[keys[i]] = users
        print(new)
print(new)
# ---------------------------------------
#new ] {" "}
# main = dict(zip(keys, users))
# print(main)

