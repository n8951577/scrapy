numbers=[12,24,35,24,88,120,155,88,120,155]
list = []
for n in numbers:
    if n not in list:
        list.append(n)
print list