# ..........inheritance

class A:

    def __init__(self):
        print('Constractor :A ')

    def f1(self):
        print('A')
class B(A):

    def __init__(self):
        print('Constructor : B')

    def f2(self):
        print('B')
class C(B):

    def __init__(self):
        super().__init__()
        print('Constructor : C')

    def f3(self):
        print('C')


a1=A()
b1=B()
c1=C()
a1.f1()
b1.f2()
c1.f3()