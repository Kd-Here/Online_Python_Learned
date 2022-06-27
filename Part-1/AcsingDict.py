"""
Self function to find value and Key pair
mydict={
    "ad":"ford",
    "bd":"Mer",
    "ca":"Bm",
    "ajd":"Pagani",
    "kd":"here",
    "kd":"world",
    "ligst":["colors","shpaes","feelings"]
    #note dict can also have key value pair of list also
}
mylist=[]
mylist2=[]
def Valu_Key():
    for i in mydict:
        mylist.append((mydict.get(i)))
        mylist2.append(i)
    print(f"The Key pair is:-{mylist2}\nThe Value pair is shown:-{mylist}")
Valu_Key()
# print(mydict.keys())
# print(mydict.values())
"""

"""
#Case to check whether key present in the dict
mydict={
    "ad":"ford",
    "bd":"Mer",
    "ca":"Bm",
    "ajd":"Pagani",
    "kd":"here",
    "kd":"world",
    "ligst":["colors","shpaes","feelings"]
    #note dict can also have key value pair of list also
}
if "Kd" in mydict:
    print("Yes present")
else:
    print("not present")
"""

"""
#TO change the list vlaues
mydict={
    "ad":"ford",
    "bd":"Mer",
    "ca":"Bm",
    "ajd":"Pagani",
    "kd":"here",
    "kd":"world",
    "ligst":["colors","shpaes","feelings"]
    #note dict can also have key value pair of list also
}
mydict["kd"]="here9899"
mydict[4]="98"
print(mydict)
"""


"""
#Method to get values from the dictionary
mydict={
    "ad":"ford",
    "bd":"Mer",
    "ca":"Bm",
    "ajd":"Pagani",
    "kd":"here",
    "kd":"world",
    "ligst":["colors","shpaes","feelings"]
    #note dict can also have key value pair of list also
}
for i in mydict.values():
    print(i)

for i in mydict.keys():
    print(i)

print("This prints both keys and values")
for i,j in mydict.items():
    print(i,j)
"""

#Nested Dictionaries
mydict={
    "ahd":{
        "name":"kd",
        "sg":"H"
    },
    "ad":"ford",
    "bd":"Mer",
    "ca":"Bm",
    "ajd":"Pagani",
    "kd":"here",
    "kd":"world",
    "ligst":["colors","shpaes","feelings"]
}
print(mydict)