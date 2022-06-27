# Case 1:- Multiple lines strings
# many="""Lorem ipsum dolor sit amet,
"""consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
"""mpr=orem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliq"""
"""print(f"{many}  {mpr}")"""


# Case 2:- Rememeber that python doesn't have character data-type
# So single character is a string of index zero

# Case 3:- Loop using in for strings 
# Code to find number of character appears in any string


# count=0
# for x in "Pseudopseudohypoparathyroidism":
#     if x=="o":
#         count+=1
# print(f"The number of times o appears is :-{count}")


# Case 4th Looping using strings 
"""for a in "The United Kingdom of Great Britain and Northern Ireland":
    print(a)"""

# Case 5th Looping to calculate character in string without space
"""count=1
for a in "The United Kingdom of Great Britain and Northern Ireland":
    print(a)
    if a!=" ":
        count+=1
print(count)"""

#Above we create our own way to calculate the length of string but we already had function to do that len()
"""
def String_Length(word):
    count=0
    for each in word:
        print(each)
        count+=1
    print(count)
a=input("Enter the string you wanter to find the length:-\n")
String_Length(a)
"""

#IS there any way to find the character present in string!
#Check character present in string