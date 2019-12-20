# .........Duck typing ->inheritance
class PyCharm:
    def execute(self):
        print('Compile')
        print('Run')

class Sublime:
    def execute(self):
        print('spell checking')
        print('conventional check')

class Desktop:

    def code(self,ide):
        ide.execute()

ide=PyCharm()
ide.execute()

D1=Desktop()
D1.code(ide)
