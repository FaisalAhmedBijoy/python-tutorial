# ..........Prime Number
n=int(input('Enter The Number'))
if (n%2 ==0 or n%3==0 or n%5==0 or n%7 ==0):
    print('Not Prime number')
else:
    print(' Prime Number')
# .............
n=int(input('Enter The Number'))
for i in range(2,n):
    if n%i ==0:
        print('Not Prime number')
        break
else:
    print('Prime Number')