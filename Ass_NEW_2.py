def count_evens(list):
    count = 0
    for i in list:
        if i%2==0:
            count=count+1
    return count
print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))