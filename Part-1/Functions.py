"""

#Arguments or Parameters are same meaning i.e. what we pass in function
#Parameter means variable we used while function definition
#Argument means the value for varibale we used while calling the function
def example(parameter) {
  print(parameter)
}
example("Argument")

example(argument);
def my_Func(a):
    print("Hello we are inside the Function whose name is",a)
my_Func("KD")
"""

"""
#If we don't known about the number of arguments then we can use *
def my_Func(*a):
    print("Hello we are inside the Function whose name is",a[1])
my_Func("KD","<f","Ge")
"""

"""
def my_Chid(a,b,c):
    print("The children are as shown:-",a)

my_Chid(a="Kd",b="gs",c="gd")


def multiplication_Table_3(a):
    for i in range(1,10):
        print(i*3)
    return a*3
print(multiplication_Table_3(10))
"""

"""
#Use * in parameter if we don't know number of arguments we will pass in same parameter

def my_kids(*kids):
    for i in range(len(kids)):
        print("The Children name are ",kids[i])

my_kids("Kd1", "Kd2", "Kd3")
"""
"""
#Use ** in parameter if\
def abca(**kid):
  print("The middle boy is named and know " + kid["second"])

abca(first = "Kd1", second = "Kd2")
"""



"""
#Recurssion Function
def fact(a):
    if a>0:
        mul=a+fact(a-1)
        print(mul)
    else:
        mul=0
    return mul
fact(10)
"""