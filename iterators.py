for i in range(10):
    print (i)
my_list = [4, 7, 0, 3]
my_iter = iter(my_list)

print(next(my_iter))
next(my_iter)

print(my_iter.next())
