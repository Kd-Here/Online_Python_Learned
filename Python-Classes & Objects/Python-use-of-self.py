# Self is used to bind classes parameter with attribute.
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.


class Car:
    # Defining attributes
    def __init__(self):
        self.name="Pagani" #  This are default parameter values we could change theml
        self.price="80M$"
        self.country="Itlay"
        self.color="user-wish"
    def comparison(self,other):
        if self.name==other.name:
            print("Both are same")
        else:
            print(f"{self.name} is the first car and another is {other.name} ")
    
    #Defining an methods

    def speed(self):
        self.speed="400Mph"
        print("The speed of "+self.name+"is :~ " +self.speed)

c1=Car()
c1.name="Buggati Centodièci"
print(f'The name of Car is {c1.name}')
c1.speed()

Rolls_Royce=Car()
Rolls_Royce.name="Rolls-Royce"
print(f'The name of Car is {Rolls_Royce.name}')
Rolls_Royce.speed()

Zonda=Car()
Zonda.color='white'
print(f"The name of Car is {Zonda.name} which cost {Zonda.price } made in {Zonda.country} and it's color is {Zonda.color}")


# We can't compare object in python by == sign bcoz it will simply compare the address of those object variable instead we want to compare the arguments of object create a funcion for that.


Zonda.comparison(c1)
