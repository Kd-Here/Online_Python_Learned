#Case 1 How to Uppercase the string which user has provided
#upper is method which UPPERCASES
"""
a=input("Enter about your self:-\n")
print(a.upper())
"""

"""
#Case 2 How to lower case the string 
print(a.lower())
"""

"""
#Case 3 How to remove white spaces from beginning and ending of string
b="   Python has a set of built-in methods that you can use on strings. "
print(b.strip())
"""

"""
#Case 4 How to remove white spaces from whole string
b="Python has a set of built-in methods that you can use on strings."
for ad in b:
    if(ad!=" "):
        print(ad,end="")
"""
from tracemalloc import start


print("\n")
#Case 5 how to replace a character from our stirng:-
"""
value="Python has a set of puilt-in methods that you can use on strings."
def char_change(b,change,replace):
    for ad in b:
        if(ad==change.upper() or ad==change.lower()):
            print(replace,end="")
        else:
            print(ad,end="")
char_change(value,"P","K")
"""


#Casee 6 Python how to find the word from string
"""
value="kython has a set of Kuilt-ikn methods that you can use on strings."
def word_find(b,find):
    count=0
    for ad in b:
        count+=1
        if(ad==find.upper() or ad==find.lower()):
            print(count)
word_find(value,"k")
"""


#Case 7 Python how to split the string if there is ' , '
"""place_hold="Hello, World! KD here"
print(place_hold.split())
"""

# Case 8 python creating function that gives str in format of list
# afs="Hello, World! KD herfe"
# print("[",end="")
# for ad in afs:
#     if ad!=" ":
#         print(ad,end="")
#         # print(f"{ad}")
#     else:
#         print("",end="")
# print("]")



#