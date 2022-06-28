# Self is used to bind classes parameter with attribute.
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.


class Car:
    # Defining attributes
    def __init__(self,name, price, country):
        self.name="Buggati"
        self.price="80M$"
        self.country="Itlay"
    
    #Defining an methods

    def speed(self):
        self.speed="400Mph"
        print("The speed of"+self.name+"is :~ " +self.speed)

Centodeicei=Car("centodièci","1B","Italy")
Centodeicei.speed()