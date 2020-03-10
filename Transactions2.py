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
for _ in range(5):
    f = names.get_first_name()
    l = names.get_last_name()
    age = random.randint(9, 50)
    t = timestampStr
    id = random.sample(range(1,5),1)
    users = [f, l, age, t, id]
    print(users)
# ---------------------------------------
# Creating the Dict with UUID
main = {uuid.uuid1(): {"firstname": f,
                       "lastname": l,
                       "age": age,
                       "date": timestampStr}}
# for x in users:
#     main[x] =