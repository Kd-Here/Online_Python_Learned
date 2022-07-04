# It's not necessaty that we should use self everytime we canhave a other vaariable also just remember it should be the first parameter of any function in class.


class Riiding:
    def __init__(ads,car,driver):
        ads.car=car
        ads.driver=driver

a=Riiding("Porsche","Kaka")
print(Riiding)
print(a)

a.car="Aston Martin"
a.driver="Mammashri"
print(a.driver)
del a.car
print(a.car)
