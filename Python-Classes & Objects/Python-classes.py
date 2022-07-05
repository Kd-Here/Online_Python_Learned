# We are usign python to solve real world problems. 
# In this world everything around you are objects! eg. man, tv, mobile, fan,ac, ball, laptop, filter, car, cup, sofa etc.

# This object has attributes i.e property & bhevauiour i.e methods.
# eg. ball has attribute as color, weight, grip. It's bhevaiour is throwing, catching.


# So what if we decided to note all ball information avaiable in Mumbai so we need to again and again use same thing i.e ball property and it's bhevaiour so tackle we use class.
# Class is blueprint or information how multiple objects can be created.

# In class we have __init__ which means in class it will have self, name, age parameters.
# https://youtu.be/qiSCMNBIP2g?t=1091



class Person:

  # this is for variables or for object property / attributes
  
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # this is for methods or bheaviour of object.
  def config():
  	print("Hi we are here")

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
Person.config()