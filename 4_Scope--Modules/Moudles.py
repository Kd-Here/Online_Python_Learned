# Modules are created to break or reuse common code i.e. funct, class, variables again in building a complex product or project

def addon(a,b):
    return a+b

def subon(a,b):
    return a-b

def mulon(a,b):
    return a*b
def divon(a,b):
    return a/b


# -----------------------------
# Fibonaci numbers where a number is sum of previous two numbers
# i.e. 
# 0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,        

# 1+1=2
# 2+1=3
# 3+2=5


def Fibo(user_input):

    count=0
    first=0
    second=1
    Fn_sum=0
    while(count<user_input):
        print(first)
        Fn_sum=first+second
        # Updating i.e setting sum of previous number is next number
        first=second
        second=Fn_sum
        # incrementing count
        count+=1





# TEST
# Fibo(10)
