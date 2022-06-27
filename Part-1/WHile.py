#No do-while loop in python but we can create it:-

# Learning break we use break to get out of current loopin
"""
i=1
while i<=90:
    print(i)
    if i==9:
        print("Yes we find it")
        break
    i+=1
"""

#We are usign continue to skip the current iteration


"""
i=0
while i<15:
    i+=1
    if i==9:
        continue
    elif i==11:
        break
    print(i)

#9 is not printed bcoz of continue
#after 10 nothing is printed bcoz we used break
"""

i=0
while i<15:
    i+=1
    if i==9:
        continue
    print(i)
else:
    print("This is printed when our loop is no longer true")