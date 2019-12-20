# # ............Formal arg & actual arg -> position ,keyword,default,variable length
def person(name,age):
    print(name)
    print(age)
person('Fasial',22)
# ...........
person(age=20, name='Bijoy')
# .........
def person(name,age=18):
    print(name)
    print('Deafult', age)
person('Ahmed',99)
# ......*b is a tuple so not addition possible int and tuple
def sum(a,*b):
    # c=a+b
    print(b)
sum(10,20,132,5614,5,6)
# .......
def mul(a,*b):
    c=a
    for i in b:
        c=c*i
    print(c)

mul(10,5,2,4)