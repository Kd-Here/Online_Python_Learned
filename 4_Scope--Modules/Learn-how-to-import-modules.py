# from Moudles import addon
from ast import Pass
from Moudles import *

a=int(input("enter the first number:-"))
b=int(input("enter the second number:-"))
print(addon(a,b))


# Here only addon funcgion is working bcox we imported only addon from moudles

# What if we wanted to use all user made moudles 
# Just simply import every i.e. *


print(subon(a,b))
print(mulon(a,b))
print(divon(a,b))




# -------------------Fibonaci code--------------------------------

va=input("Type Yes if wanted to see Fibonaci series!")
if va =="Yes":
    Number=int(input("Enter the term till which we should print Fibonaci code:-\n"))
    print(Fibo(Number))
else:
    print("Thnaks for uworking with us")