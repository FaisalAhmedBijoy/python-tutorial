# ..............method overloading
class Student:

    def sum(self,a=None,b=None,c=None):

        c=0
        if a!=None and b!=None and c!=None:
           c=a+b+c
        elif a!=None and b!=None:
            c=a+b
        else:
            c=a
        print(c)


s1=Student()
s1.sum(10,20,30)
s1.sum(10,20)
s1.sum(48)