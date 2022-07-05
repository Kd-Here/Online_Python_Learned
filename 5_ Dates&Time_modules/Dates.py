import datetime

#datetime is module to check the content of any module use dir(module_name)
print(dir(datetime))


# a is an object first datetiem is module name and 2nd datetime is class name and now is the method of class.
a=datetime.datetime.now()
print(a)


# ------------------------------------------------------ 
# we can also avoid using first datetime by mention the correct module to import

# from datetime import datetime,date
# b=datetime.now()
# print(b)


# # Method to change oor set date
# ca = date(2022, 2, 13)
# print(ca)