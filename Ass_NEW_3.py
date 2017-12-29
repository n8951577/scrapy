def centered_average(list):
    a=b=average = 0
    sum = 0
    for n in list:
        sum = sum + n
        a=max(list)
        b=min(list)
        average = (sum - a - b) / (len(list) - 2)
    return (list,a,b,average)
print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))
