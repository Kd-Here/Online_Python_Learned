class Father:
    def __init__(self,first_name,sirname):
        self.first_name=first_name
        self.sirname=sirname
        print("Entered here")
    def say_my_name(self):
        print(f"Hi sir your full name is{self.first_name} {self.sirname}")

class Child(Father):
    def __init__(self,ch_first_name,ch_sirname):
        print("Hi i want to konw who I am")
    
        super().__init__(ch_first_name,ch_sirname)

# ob=Child("Mike", "Olsen")
ob=Father("m","O")
ob.say_my_name()