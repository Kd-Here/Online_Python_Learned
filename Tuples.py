"""
#Creating a tuple and showing it's type
mytuple = ("abc", 34, True, 40, "male")
print(mytuple)
print(type(mytuple))


#Accessing the Tuples element
mytuple = ("abc", 34, "Kdhere",True,"9899" ,40, "male")
# print(mytuple[2:])
if "Kdhere" in mytuple:
    print("Yes it's present there!")

#We can't add value to tuple it's immutable. But we cheat around convert tuple in list and then convert it to tuple back again
mytuple[4]=="9"
print(mytuple)


mytuple = ("abc", 34, "Kdhere",True,"9899" ,40, "male")
k=list(mytuple)#This is to convert list to tuple
k[4]="8gha"
mytuple=tuple(k)
print(mytuple)

#Case to remove the element from our tuple
mytuple = ("abc", 34, "Kdhere",True,"9899" ,40, "male")
dd=list(mytuple)
dd.pop(4)
mytuple = tuple(dd)
print(mytuple)



#case Upacking of tuples
fruits=("aam","Kela","Seb","sitaphal",'angur')
(red,*yellow,orange)=fruits
print(red,yellow,orange)



#Case to loop through tuple
fruits=("aam","Kela","Seb","sitaphal",'angur')
for i in range(len(fruits)):
    print("Fruit name is:-",fruits[i])


Phal=["aam","Kela","Seb","sitaphal",'angur']
for i in range(len(Phal)):
    print(Phal[i])

#While loop for iterating through tuples
Phal=["aam","Kela","Seb","sitaphal",'angur']
i=0
while i<len(Phal):
    print(Phal[i])
    i+=1

"""
# Creating counter for numbers in tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
def my_Counter(a):
    cont=0
    for i in thistuple:
        if i==a:
            cont+=1
    print(f"The count of the number is,{cont}")
my_Counter(5)
