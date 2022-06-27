#Case 1 Insert Items in list


mylist=["list can have different data-type","KD",9,9.899,True]
# mylist.insert(2,"Kdhere")
# print(mylist)


#Case 2 Append is used to add element at last of list whereas insert is used to add any position

# We used insert to insert at last in short create our append:-
"""
length=len(mylist)
def list_ad(a,b):
    mylist.insert(a,b)
list_ad(length,"I am at last")
print(mylist)
"""

"""
#Case 3 adding entire list to another list THIS IS DONE BY METHOD NAME extend"
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

for i in thislist:
    mylist.append(i)
for i in thistuple:
    mylist.append(i)
print(mylist)
"""

# Case 4 Removing elements from List
"""
mylist.remove("KD")
print(mylist)

#Case 5 if we wanted to remove element at particular index
mylist.pop(2)
print(mylist)

#Case to removes all element in list used clear
mylist.clear()
print(mylist)
"""
