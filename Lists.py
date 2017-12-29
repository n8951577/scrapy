list = ['abcd',123,45.6,-23,'kirana']
list1 = [123,'Kirana']

if list == 'Kirana':
    print("pass")
else:
    print("fail")

x=list[1]
print("The value of list is",x)
y=list[-2]
print("The value in reverse order of the list is",y)


url="https://www.google.com/impelsys/careers.html/"
page=url.split("/")
page1=url.split("/")[-2]
print(page)
print(page1)

hai="0000000sjdpsajd0d0safdsaf0afa0f0dsaf0a0fa000000"
page3=hai.strip("0")
print(page3)

#Delete an items in a list
a=[1,2,3,4]
del(a[2])
print(a)

print(a,10,3.3)

#Insert a items to a existing list
list2=["Kiran","Pavan","Chetan"]
print(list2)
list2.insert(0,"Praveen")
print(list2)
print(list2[2])
print(list2[-1])

#Search an items in the list
print(list2.index("Kiran"))
print(list2.index("hai"))
