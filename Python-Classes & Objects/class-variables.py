# Classes in python 2 variables 1) instant vairable which we define usiing __init__
# Second varibales are which decclared outside the class are class variable if we change value of class variable it will be same for all object of that class

class Car:
    #Variables define here are class variabels
    wheels=4

    def __init__(self):
        self.name="Pagani" #  This are default parameter values we could change theml
        self.price="80M$"
        self.country="Itlay"
        self.color="user-wish"




Car.wheels=2

c1=Car()
c1.name="Buggati Centodièci"
print(f'The name of Car is {c1.name} Wheels are {c1.wheels}')

# Run this code before commiting  and after 


Rolls_Royce=Car()
Rolls_Royce.name="Rolls-Royce"
print(f'The name of Car is {Rolls_Royce.name} Wheels are {Rolls_Royce.wheels}')
