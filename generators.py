
# ...............Generators
print('Generator ....')
def top():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n=n+1


values=top()
print(values)
for i in values:
    print(i)