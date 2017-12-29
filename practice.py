def addition(x, y):
    return x + y
def subtraction(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def division(x, y):
    return x / y

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = input("Enter the options:")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if choice == '1':
    print(a,"+",b,"=", addition(a,b))

elif choice == '2':
    print(a,"-",b,"=", subtraction(a,b))
elif choice == '3':
    print(a,"*",b,"=", multiplication(a,b))

elif choice == '4':
    print(a,"/",b,"=", division(a,b))
else:
    print("Invalid input")
