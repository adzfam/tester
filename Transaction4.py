import random
import uuid
import names
from datetime import datetime

# from faker import Faker


# for the values to be the same for both dictionaries they must be placed
# within the same for loop
# i don't know if this is saving each dict from the for loop individually
# or only showing me the latest loop.
# how do i refer back to the dict and call a specific key/value pair
# to later use in a different dictionary
# the step to create transactions between different people is where im stuck
#
for _ in range(5):
    f = names.get_first_name()
    l = names.get_last_name()
    age = random.randint(15, 50)
    dt = datetime.now()
    id = uuid.uuid1()
    timestampStr = dt.strftime("%d-%b-%Y")
    trans = {"ID": id,
             "firstname": f,
             "lastname": l,
             "Budget": "Is left with £100",
             "date of transaction": timestampStr}
    print(trans)
    # TODO: HOW CAN I PUT ALL THESE VALUES IN A BIG DICT,
    main = {"ID": id,
            "firstname": f,
            "lastname": l,
            "age": age,
            "date": timestampStr}
    print(main)
    print("--")
# TODO: HOW CAN I PUT ALL THESE VALUES IN A BIG DICT,
# THEY ARE ALL COMING OUT AS INDIVIDUAL DICTS

# super_main = {}
# for i in main.keys():
#     for j in zip(main.values(),main.values()
