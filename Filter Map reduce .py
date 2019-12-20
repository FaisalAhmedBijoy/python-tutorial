# Filter map Reduce
from functools import reduce
def is_even(n):
    return n%2==0

def update(n):
    return n*2

def add_all(a,b):
    return a+b
nums=[1,2,55,44,5,6,45,5,5,4,4,4,5,55]
# evens=list(filter(is_even,nums))
evens=list(filter(lambda n:n%2==0,nums))
print('Even number : ',evens)

# double=list(map(update,evens))

double=list(map(lambda n:n*2,evens))
print('Double Number : ',double)

#  For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
#     ((((1+2)+3)+4)+5)
# sum=reduce(add_all,double)
sum =reduce(lambda a,b:a+b ,double)
print('Sum is : ',sum)