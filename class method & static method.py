#class method & static method
class Student:
    school='telusko'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print('This is Static Student')

s1 = Student(10 ,20,40 )
s2 =Student( 5 ,66,22 )
print(s1.avg())
print(s2.avg())

print(Student.getSchool())

print(Student.info())