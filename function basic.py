def hello():
    print('Hello World')

def add_sub(x,y):
    a=x+y
    b=x-y
    return a,b
def update(x):
    print('x', x)
    print('x id',id(x))
    x=15 ;
    print('x new id',id(x))
hello()
result1,result2=add_sub(5,6)
print(result1 ,result2)

a=10
update(a)
print('a',a)
print('a id',id(a))
