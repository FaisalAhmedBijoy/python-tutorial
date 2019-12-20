#Recursion
def fact(n):
    if n==0:
        return 1
    return  n* fact(n-1)
n=int(input('Enter The number'))
result=fact(n)
print('Factorail of : {} is :{}'.format(n,result))