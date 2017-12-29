1.
def square():  
    n=list()
    for i in range(1, 21):
        n.append(i ** 2)   
    print("Full List:",n)
    print("Start from 5th Index",n[5:])
square()    

2.
def square():  #function defn
    n=dict()
    for i in range(1, 21):
        n[i] = i ** 2   
    print(n)
square()    #function Call

3.
def square():  
    n=dict()
    for i in range(1, 4):
        n[i] = i ** 2   
    print(n)
square()   

4.
def number():
    n=int(input("Please enter a Number"))
    if(n%2==0):
        print("Even Number")
    else:
        print("Odd number")
number()

5.
list=[]
for n in range(2000, 3201):
    if (n%7==0) and (n%5!=0):
        list.append(n)
print(list)

6.
list=[12,24,35,70,88,120,155]
print("Before removing a elements in the list",list)
list=[val for (idx,val) in enumerate(list) if idx not in (0,4,5)]
print("After removing a elements in the list",list)

7.
numbers=[12,24,35,24,88,120,155,88,120,155]
list = []
for n in numbers:
    if n not in list:
        list.append(n)
print list
