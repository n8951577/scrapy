"""
By default sys.argv values will be string and we have to convert to int based on our requirement
We have to use sys module
File name also will be counted as part of sys.argv list item
"""

import sys

def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def mul(a,b):
    return(a*b)

def div(a,b):
    return(int(a/b))

def airth(number1,number2,operator):
    if(operator == "+"):
        return add(number1,number2)
    elif(operator == "-"):
        return sub(number1,number2)
    elif(operator == "*"):
        return mul(number1,number2)
    elif(operator == "/"):
        return div(number1,number2)
    else:
        return 0

if __name__ == "__main__":
    args = sys.argv
    print(type(args))
    print(args)

    if len(args)==4:
        print(airth(int(args[1]),int(args[2]),args[3]))
    else:
        print("Not enough args")