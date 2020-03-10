import random
import uuid
import names
from datetime import datetime
#from faker import Faker



for _ in range(10):
    f = names.get_first_name()
    l = names.get_last_name()
    age = random.randint(5, 20)
    dt = datetime.now()
    id = uuid.uuid1()
    timestampStr = dt.strftime("%d-%b-%Y")
    main = {"ID": id,
            "firstname": f,
            "lastname": l,
            "age": age,
            "date": timestampStr}
    print(main)

#TODO: HOW CAN I PUT ALL THESE VALUES IN A BIG DICT,
# THEY ARE ALL COMING OUT AS INDIVIDUAL DICTS

# super_main = {}
# for i in main.keys():
#     for j in zip(main.values(),main.values()