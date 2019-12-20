class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('Core i5 , 16GB RAM', self.ram, self.cpu)


com1 = Computer('Ryzen', 16)

com1.config()


class Car:
    wheels = 4
    com = 'AAA'
    mil = 33

    def __init__(self):
        self.com = 'BMW'
        self.mil = 10


c1 = Car()
c2 = Car()

c1.com = 'Audi'
Car.wheels = 48
print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)