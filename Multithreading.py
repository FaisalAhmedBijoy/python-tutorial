# ...............Multithreading ...........
from time import  sleep
from  threading import *
class Hello(Thread):
    def run(self):
        for i in range(10):
            print('Hello')
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(10):
            print('Hi')
            sleep(1)

t1=Hello()
t2=Hi()
t1.run()
sleep(.2)
t2.run()

t1.start()
t2.start()

print('bye')
