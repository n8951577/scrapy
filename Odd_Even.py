print('Print the Odd or Even Numbers')
num = int(input('Enter a Number'))
print('User entered Number is %d' % num)
try:
    if (num % 2):
        print('Number is Even number')
    else:
        print('Number is odd')
except:
    print('Entered a Wrong number Please Check once...!')
