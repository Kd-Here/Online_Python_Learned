import time
from datetime import datetime
print(dir(time))

# IT'S bestly used when we are using multithreading to stop a given process use sleep
print("This is printed immediately.")
time.sleep(2.4)
print("This is printed after 2.4 seconds.")

# Want to print time like a actual clock this is how you can do it.

while True:
    a=datetime.now()
    time.sleep(1)
    print("%s/%s/%s %s:%s:%s" % (a.month,a.day,a.year,a.hour,a.minute,a.second)) 

