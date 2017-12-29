from myModule import Person  # Import a particular Modules  [myModule.py]
from myPackages.Car import *   #import all the Modules inside the own created packages    [myPackages/Car.py]

Person1 = Person()
Person1.name ='Kiran'
Person1.sayHello()


myCar = Car()
myCar.setSpeed(100)

myTruck = Truck()
myTruck.setSpeed(100)
