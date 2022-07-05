from audioop import reverse
import csv


#With means when you open 'file.csv' file in 'r' mode i.e. read stored in vairable see
#for_opening is variable which calls the method csv reader whos argument is our variable who is storing data of csv file
# next is used to skip the first row which contains the title for our sheet
# lastly we used for loop to iterate through our file
# with open('file.csv','r') as see:
#     for_opening=csv.reader(see)
#     next(for_opening)
#     for i in for_opening:
#         print(row[1])



""" Alternatively more robust method to do that is Dict reader to avoid error if someone change columns name without changing content:-
#with opening the file.csv in read mode stored in variable storage
displaying the content in DictReader format of stored variable storage
for is used to iterate throughout our variable displaying
we are printinh the row whose falls under title check file.csv for refference
"""


# with open('file.csv','r') as storage:
#     displaying=csv.DictReader(storage)
#     for row in displaying:
#         print(row['title'])



"""Here we are trying to avoid the duplicate value of
tried but fail :-first we create a list and append all the value
after that we create set of that list using set constructor 
but there was gotcha set's are unordered yeah they don't store duplicates value but still found some value
Wrong code:-

mylist=[]
#with open('file.csv','r') as storage:
#     displaying=csv.DictReader(storage)
#     for row in displaying:
#         mylist.append(row['title'])

myset=set(mylist)
for i in myset:
    print(i)


"""

mylist={}
with open('file.csv','r') as storage:
    displaying=csv.DictReader(storage)
    for row in displaying:
        i=row['title'].upper().strip()
        if not i in mylist:
            mylist[i]=0 
        mylist[i]+=1

def getting_values(for_given_title):
    return mylist[for_given_title]


#Here we are sorting our list in reverse order but on the basis of getting_values function
# means that function gives the value(number of voted) for corresponding key(title) here 
#SInce we can't sort dict on basis of our values key sorting is always possible

for a in sorted(mylist, key=getting_values, reverse=True):
    print(a,mylist[a])





"""
#Personal code to sort dictionary on basis of values:-
def get_key(val):
    for key, value in mylist.items():
         if val == value:
             return key
 
    return "key doesn't exist"
 
 
for a in sorted(mylist.values(),reverse=True):
    print(get_key(a),a)

"""


    

"""
#Sorting on basis of values using lambda function
What is lambda function:) a function with no name i.e. anyomous function!

lamda is doing same as this function but we don't needed name for function, argument names, return statement
def getting_values(for_given_title):
    return mylist[for_given_title]

for a in sorted(mylist, key=lambda ass:mylist[ass], reverse=True):
    print(a,mylist[a])
"""

