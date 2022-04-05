"""
set1 = {"abc", 34, True, 40, "male"}
print(len(set1))
print(type(set1))

#we can also use set constructor like others data-type constructor's
set43=set(("apple", "banana", "cherry"))
print(set43)


# CaseTrying to add and to change value of set
set43=set(("apple", "banana", "cherry"))
print("banana" in set43)
# set43[2]="jackfruit"We can't change value of set's put we can add values to tupel
print(set43)
set43.add("8")
print(set43)

#Case we adding othere type of letrals to our sets
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

mysd=set((mylist))
for i in mysd:
    thisset.add(i)
print(thisset)
"""


