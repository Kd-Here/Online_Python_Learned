from calendar import month
from inspect import getmembers
import threading 
import time
  
def print_hello():
  for i in range(4):
    time.sleep(0.5)
    print("Hello")
  
def print_hi(): 
    for i in range(4): 
      time.sleep(0.7)
      print("Hi") 


t1 = threading.Thread(target=print_hello)  
t2 = threading.Thread(target=print_hi)  
t1.start()
t2.start()


threading.active_count()
# Thread is the class remember using and module type print(dir(threading))
# All caps starter are class name and all other small are methods or attributes or functions