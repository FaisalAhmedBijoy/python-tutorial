# factorial

def factorial(n):
    fact=1
    if n==0:
        print(1)
    else:
        for i in range(1,n+1):
            fact =fact*i

    return fact


n=int(input('Enter The  Number'))
answer=factorial(n)
print("Factorial of the Number : ",n,'is : ',answer)