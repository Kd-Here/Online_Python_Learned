"""Python does not have a random() function"""
"""Be sure not to name your file this file name as random.py 
you will get and error like this 
partially initialized module 'random' has no attribute 'randrange' (most likely due to a circular import)
"""
import random
a=random.randrange(1,100)
print(a)