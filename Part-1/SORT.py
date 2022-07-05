#We had an method to sort the elements in list alphabetically, or ascending
#here for sorting we should posses all the elements in same data-type

"""
mylist=["list can have different data-type","KD","9","9.899","True"]
mylist.sort()
print(mylist)

#Here we are checking the sorting for interger
mylist=[100, 50, 65, 82, 23]
mylist.sort()
print(mylist)

#Reversing the order of sorting
mylist=[100, 50, 65, 82, 23]
mylist.sort(reverse=True)
print(mylist)
"""


#Sort and using key value pair
#Here abs is function which gives the absolute value of argument
def mysort(n):
    return abs(n-50)
mylist=[100, 50, 65, 82, 23]
mylist.sort(key=mysort)
print("This is return list:-",mylist)