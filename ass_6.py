list=[12,24,35,70,88,120,155]
print("Before removing a elements in the list",list)
list=[val for (idx,val) in enumerate(list) if idx not in (0,4,5)]
print("After removing a elements in the list",list)