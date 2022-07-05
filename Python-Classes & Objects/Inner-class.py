# Inner class can be access by calling outer class. innerclass 



class Car:
    
    wheels = 4
    def __init__(self):
        self.name="Pagani" #  This are default parameter values we could change theml
        self.color="user-wish"
        # self.kd= self.more()

    def show(self):
        print(f'The name of Car is {self.name} Wheels are {self.wheels}')
    
    # @classmethod
    # def __init__(cls):
    #     cls.Name="Buggati!"
    #IF wanted to use outer class parameter in inner class.

    # Inner class
    class more:
        
        def __init__(self):
            self.model="Kd"
            self.origin="Kd"

        def show(self):
            print(f'\nThe {Car.Name} model {self.model} has {Car.wheels} wheels and carfted in {self.origin}')



c1=Car()
c1.name="Buggati"
c1.show()

# Creatin an object of inner class as :- variable = Outer_Class.Inner_Class
ad=c1.more()
ad.model="Centodièci"
ad.origin="Italy"
ad.show()



Rolls_Royce=Car()
Rolls_Royce.name="Rolls-Royce"
Rolls_Royce.show()