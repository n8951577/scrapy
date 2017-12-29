def square():  #function defn
    n=list()
    #i=int(input("enter an order"))     #User Input
    #for i in range (0,i):
    for i in range(0,21):
        n.append(i ** 2)   #exponential
    print("Full List:",n)
    print("Start from 5th Index",n[5:])
square()    #function Call