# from subprocess import CalledProcessError


# # Method overloading when we are have methods of same name how will compiler know which method is Called 
# # so compiler checks for number of parameters if there is method with 2 parameter it will be called by obj.method by passing 2 parameters.bytearray
# # same for 3 or 4



# class A():
#     def __init__(self):
#         pass


#     def sum(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             s=a+b+c
#             return s
#         elif a!=None and b!=None:
#             s=a+b
#             return s
#         else:
#             return a

# ass=A()
# print(ass.sum(9,9,9))
# # here check compiler checking of number of parameter passed!
# print(ass.sum(98,99))






# # <!--->

from ast import MatchSequence


# Methodoveriding :- When we don't have a method in child class but an object of child class calls it so it will overide to parent method if it's MatchSequence

class A():
    def show(self):
        print("i am in A")

class B(A):
    pass
#See in b we currently don't have a method name show but as sit i a childof A it will extend or it will overides th epaarent inti

ocj=B()
ocj.show()