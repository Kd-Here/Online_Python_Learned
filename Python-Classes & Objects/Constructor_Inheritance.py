# How class and their constructor are called in python  
# In Python the __init__() method is called the constructor and is always called when an object is created

class A():
    def __init__(self):
        print("I am constructor of A")

    def method1(slef):
        print("Function 1 is working")
    
    def method2(slef):
        print("Function 2 is working")

class B(A):
    def __init__(self):
        super().__init__()
        # This Super calls the parent class method __init__ ()    i.e  constructor of parent class 
        print("I am constructor of B")
    def method3(slef):
        print("Function 3 is working")
    
    def method4(slef):
        print("Function 4 is working")


c1=B()
# This will call the constructor or __init__method of class B


# How to call parent constructor from object of child use Super()