from random import random
import uuid
import names
f = names.get_first_name()
#print(f)
l = names.get_last_name()
v = {}
for x in range(5):
 f = names.get_first_name()
 l = names.get_last_name()
 a = random()

 v[uuid.uuid1()] = {"firstname":f, "lastname":l,"age": a}
print(v)

columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in v.keys())
values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in v.values())
sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('mytable', columns, values)
print(sql)
