#.........operator overriding

class A:
    def show(self):
        print('in A here')

class B(A):
    pass

a1=B()
a1.show()