def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)
try:
    n = int(input("enter a number to find the factorial of a digit"))
    print ("The factorial of n is %d" % factorial(n))
except:
    print("Invalid")