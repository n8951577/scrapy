def big_diff(list):
    max = list[0]
    min = list[-1]
    for n in list:
        if max < n:
            max = n
        if min > n:
            min=n
    return max,min,max-min
print big_diff([10, 3, 5, 6])
print big_diff([7, 2, 10, 9])
print big_diff([2, 10, 7, 2])