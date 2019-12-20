# .......................Itrator
num=[5,6,10,4,7,10]

for i in num:
    print(i)

it=iter(num)
print(it)
print(it.__next__())
print(it.__next__())
print('My iterator in class')
class TopTen:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10 :
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration

values=TopTen()
print(values.__next__())
print(next(values))

for i in values:
    print(i)