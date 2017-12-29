class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total employee is  %d" %Employee.empCount)

    def displayEmployee(self):
        print ("Name:",self.name,"and Salary:", self.salary)

#Creating an Instance of an objects
emp1 = Employee('Kiran', 20000)
emp2 = Employee('Praveen', 28000)

#Accessing Attributes By using .(dot) operator
emp1.displayEmployee()
emp2.displayEmployee()

#Display an Total count of an employees
print("Total employees are  %d" % Employee.empCount)



#In-built functions
hasattr(emp1,'Kiran')
getattr(emp1,'Kiran')
setattr(emp1,'Kiran','Pavan')
delattr(emp1,'Kiran')

