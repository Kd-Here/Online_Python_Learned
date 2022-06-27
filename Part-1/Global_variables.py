"""Variables declared out of function are termed as global variables"""


"""#Since a is defined outside of function it's global and can have acess to funct also
a="Learning Python"
 
def myfuct():
    a="Learning Js"
    #Now this is variable inside function so with same global name it's overwrite

    print(f"WISH YOU The who is,{a}")
# myfuct(A)This is different remembered python is case sensitive
myfuct()
"""


#Case 3 Declaring infunction variable as global
"""a="Learning Python"
 
def myfuct():
    global a
    a="Learning Js"
    #Now this is variable inside function so with same global name it's overwrite

    print(f"WISH YOU The who is,{a}")
# myfuct(A)This is different remembered python is case sensitive
myfuct()
print(f"are you loving it? ,{a}")
"""


# Case 4