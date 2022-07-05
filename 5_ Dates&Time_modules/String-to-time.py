# When we provide a string format date Python strptime() can convert it to time format

from datetime import datetime, date

date_in_string = "08 August, 2001"
date_object = datetime.strptime(date_in_string, "%d %B, %Y")
print(date_object)



dt_string = "8/08/01 12:15:32"
data_objec =datetime.strptime(dt_string,"%d/%m/%y %H:%M:%S")
print(data_objec)