n=int(input("Enter a number"))

i=1
while i<=n:
    print('#',end="")
    j=1
    while j<=i:
        print('#',end="")
        j=j+1
    i=i+1
    print('\n')