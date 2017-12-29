data = int(input("Enter a length of diamond to be formed: "))

for x in list(range(data)) + list(reversed(range(data-1))):
    print('{: <{d1}}{:*<{d2}}'.format('', '', d1=data-x-1, d2=x*2+1))
