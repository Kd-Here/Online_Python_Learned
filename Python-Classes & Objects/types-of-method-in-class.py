# in python 3 types of method 
# which are class method, static and instantenous method

class Car:
    wheels=4

    def __init__(self):
        self.name="Pagani" #  This are default parameter values we could change theml
        self.price="80M$"
        self.country="Itlay"
        self.color="user-wish"



#The class method will have @classmethod which will remain same for all the objects of our class.
        @classmethod
        def getwheels(cls):
            print(f"The wheels {self.name} of are {cls.wheels}")
        
#Static method are those nothing to deal with object attributes or methods they are not invovlement in the class!
        @staticmethod
        def forCar():
            print("Hi")
            print(f" currently can't fly" )


        # This is instant method
    def comparison(self,other):
        if self.name==other.name:
            print("Both are same")
        else:
            print(f"{self.name} is the first car and another is {other.name} ")


c1=Car()
c1.name="Buggati Centodièci"
print(f'The name of Car is {c1.name}')



Rolls_Royce=Car()
Rolls_Royce.name="Rolls-Royce"
print(f'The name of Car is {Rolls_Royce.name}')

# Car.getwheels(Car)
Car.forCar()
