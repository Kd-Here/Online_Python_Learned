# asd="HEy GoodMOrning"

# def Greeting():
#     asd="Good AfterNOon"
#     # This asd has a local scope till the end of function
#     print(asd)

# Greeting()
# print(asd)


# ------------------------------------------------------------------------!_-----------------------------------------------------------


global asd
asd= "HEy GoodMOrning"

def Greeting():
    # This asd has a local scope till the end of function
    print(asd)

Greeting()
print(asd)