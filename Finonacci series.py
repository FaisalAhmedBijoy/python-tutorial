#fibonacci series
def fibo(n):
    a=0
    b=1
    if n<=0:
        print('No number ')
    elif n==1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
n=int(input('Enter The total Number'))
fibo(n)