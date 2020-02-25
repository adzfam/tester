#setting up and installation of pycharm, pyhton and conda

#Begin with

#Print
print("Hello World")
#the object will be converted into a string before written to the screen.
print(42)                            # <class 'int'>
#42
print(3.14)                          # <class 'float'>
#3.14
print(1 + 2j)                        # <class 'complex'>
#(1+2j)
print(True)                          # <class 'bool'>
#True
print([1, 2, 3])                     # <class 'list'>
# [1, 2, 3]
print((1, 2, 3))                     # <class 'tuple'>
# (1, 2, 3)
print({'red', 'green', 'blue'})      # <class 'set'>
# {'red', 'green', 'blue'}
print({'name': 'Alice', 'age': 42})  # <class 'dict'>
# {'name': 'Alice', 'age': 42}
print('hello')                       # <class 'str'>
# hello

#---------------------------------------------------------------
#List
#List is a collection which is ordered and changeable.
# Allows duplicate members.

#Create a List:
thislist = ["apple", "banana", "cherry"]   #Note the square brackets
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #Print the second item of the list
thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist1[2:5]) #Return the third, fourth, and fifth item:

thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist2[:4])
#This will return the items from index 0 to index 4.
#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included

#Change the second item:
thislist3 = ["apple", "banana", "cherry"]
thislist3[1] = "blackcurrant"
print(thislist3)

#Print all items in the list, one by one:
thislist4 = ["apple", "banana", "cherry"]
for x in thislist4:
  print(x)

#Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Using the append() method to append an item:
thislist5 = ["apple", "banana", "cherry"]
thislist5.append("orange") #adds this item to the end of the list
print(thislist5)

#Inserts in a specfic location
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange") #Insert an item as the second position:
print(thislist)

#The remove() method removes the specified item:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#The pop() method removes the specified index,
# (or the last item if index is not specified):
thislist7 = ["apple", "banana", "cherry"]
thislist7.pop() #number in the bracket specifies the place
print(thislist7)
#del function does the same and you can also delete the whole list using
del thislist7

#Make a copy of a list with the copy() method:
thislist8 = ["apple", "banana", "cherry"]
mylist1 = thislist8.copy()
print(mylist1)

#Join two list:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
#adds the second list after the first
list3 = list1 + list2
print(list3)
#or
list1.extend(list2)
print(list1) #this does the same thing without creating a 3rd list


#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list

#----------------------------------------------------------------
#Tuple
#Tuple is a collection which is ordered and unchangeable.
#Allows duplicate members.
#Tuples are sequences, just like lists.
thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuplee = ("apple", "banana", "cherry")
print(thistuplee[1]) #(+) value starts from beginning
#Remember that the first item is position 0
print(thistuplee[-1]) #prints last item of tuple. (-) begins from end
thistupleee = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistupleee[2:5]) #prints range
#position 5 is not included, but 2 is
# The differences between tuples and lists are, the tuples cannot be changed
# unlike lists and tuples use parentheses, whereas lists use square brackets.
# Creating a tuple is as simple as putting different comma-separated values.

x = ("apple", "banana", "cherry") #create tuple
y = list(x)   #convert tuple to list to be able to edit it
y[1] = "kiwi" #change value 1 to different name
x = tuple(y)   #sets new variable as this new list

#Check if "apple" is present in the tuple:
thistuple1 = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
print(x)

#Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#--------------------------------------------------------------------------
#Sets
#Set is a collection which is unordered and unindexed.
#No duplicate members.
# set()
# TODO: make it a proper set
thisset = {"apple", "banana", "cherry"}
thisset2 = {"apple", "cherry"}

#shows the union of both sets
new_set = thisset & thisset2

print(thisset)
# Note: the set list is unordered,
# the items will appear in a random order.

#---------------------------------------------------------------------------
#Dictionary
#Dictionary is a collection which is unordered, changeable and indexed.
# No duplicate members.

#dictionaries are written with curly brackets
#and they have keys and values.
#Create and print a dictionary:
carsdict =	{
#   key  :  value
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(carsdict)  #shows the full dictionary

#Get the value of the "model" key:
x = carsdict["model"] #shows the value associated with the key 'model'

#Change a value in a specific key
carsdict["year"] = 2018 #Change the "year" to 2018
print(carsdict)  #shows the new dictionary

#Use for loop to show the keys in a dictionary one by one in one column
for x in carsdict:
  print(x)

#Print all values in the dictionary, one by one:
for x in carsdict:
  print(carsdict[x]) #notice the difference between the above SQUARE BRACKETS

#Loop through both keys and values, by using the items() function:
for x, y in carsdict.items():
  print(x, y)  #prints both keys and values in one column (key  value)

#Check if "model" is present in the dictionary:
#searching dictionary using if statement
if "model" in carsdict:
  print("Yes, 'model' is one of the keys in this dictionary")

#find how many items (key-value) pairs are in a dictionary
#len()
print(len(carsdict))

#adding items to a dictionary
carsdict["colour"] = "red"   #adds this new item to the end of the dictionary
print(carsdict)

#to delete an item belonging to a specific key
#pop()
carsdict.pop("model") #deleting model item from dictionary
print(carsdict)
#does the same thing
del carsdict["colour"]  #if you dont specify the [""] key it'll delete the whole dict
print(carsdict)


#-----------------------

#Variables

#if statements

#for loops

#functions

