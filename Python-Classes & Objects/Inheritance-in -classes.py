# There are 3 types of inheritance 1) Single level inheritances i.e have single parent and child
#   2) Mulitlevel level inheritances i.e. have great grandparent ...grandparent, parent and child
#   3) Multiple  inheritances i.e can extend/inherit different classes.



# 1) Single level inheritances i.e have single parent and child
# class A():
#     def method1(slef):
#         print("Function 1 is working")
    
#     def method2(slef):
#         print("Function 2 is working")

# # B is extend/ inheriting A
# class B(A):
#     def method3(slef):
#         print("Function 3 is working")
    
#     def method4(slef):
#         print("Function 4 is working")
# # B is sub class and A is parent class
# c1=B()
# c1.method1()
# c1.method3()




#   2) Mulitlevel level inheritances i.e. have great grandparent ...grandparent, parent and child
# class A():
#     def method1(slef):
#         print("Function 1 is working")
    
#     def method2(slef):
#         print("Function 2 is working")

# # B is extend/ inheriting A
# class B(A):
#     def method3(slef):
#         print("Function 3 is working")
    
#     def method4(slef):
#         print("Function 4 is working")

# # C is inheriting/extending B which is further extending A
# class C(B):
#     def method5(self):
#         print("Function 5 is working")

# c1=C()
# c1.method1()
# c1.method3()
# c1.method5()


#   3) Multiple  inheritances i.e can extend/inherit different classes.

class A():
    def method1(slef):
        print("Function 1 is working")
    
    def method2(slef):
        print("Function 2 is working")

class B():
    def method3(slef):
        print("Function 3 is working")
    
    def method4(slef):
        print("Function 4 is working")

# C is inheriting/extending A  And also B
class C(A,B):
    def method5(self):
        print("Function 5 is working")
        
c2=B()
c2.method3()


c1=C()
c1.method1()
c1.method3()
c1.method5()