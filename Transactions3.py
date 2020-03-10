import random
import uuid
import names
from datetime import datetime
from faker import Faker

fake = Faker()
dt = datetime.now()
timestampStr = dt.strftime("%d-%b-%Y")
f = names.get_first_name()
l = names.get_last_name()
age = random.randint(9, 50)
t = timestampStr
id = uuid.uuid1()

for _ in range(2):
    f = names.get_first_name()
    l = names.get_last_name()
    age = random.randint(9, 50)
    t = timestampStr
    id = uuid.uuid1()
    users = [id, f, l, age, t]
    keys = ["ID", "first name", "last name", "age", "time"]
    print(users)

dictionary = dict(zip(keys, users))
print(dictionary)