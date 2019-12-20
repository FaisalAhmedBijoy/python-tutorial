#inner class
class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.Laptop()
    def show(self) :
        print('Name : {} , Roll : {} '.format(self.name,self.roll))
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram=8
        def show(self):
            print('Brand : {} , CPU : {} , RAM :{} GB '.format(self.brand,self.cpu,self.ram))



s1=Student('Navin',11)

s1.show()

lap1=Student.Laptop()
lap1.show()