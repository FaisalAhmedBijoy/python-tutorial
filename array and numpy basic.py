import array
val=array.array('i',[1,2,3,4,5,6])

for i in val:
    print(i)

from  array import *
import numpy
val=array('i',[10,20,30,40])
for i in val:
    print(i)


print('Memory Allocation', val.buffer_info())
newArray =array(val.typecode,(a for a in val) )
print(newArray)

num =array('i',[])
n=int(input('Enter the total number of the array'))
for i in range(n):
    x=int(input('Enter a number'))
    num.append(x)
print(num)

s=int(input('Enter a number to search'))
k=0
for i in range (n):
    if s==num[i]:
        print('Number found index',num.index(x))
        break
else:
    print('Number is not found')

print('Array Elements are')
for i in num:
    print(i)
from numpy import *
arr=array([1,2,3])
print(arr.dtype)
print(arr)

arr= array([10,20,'faisal'],str)
print(arr)
print(arr.dtype)

arr=linspace(10,20,5)
print(arr)

arr=arange(10,100,5)
print(arr)

arr=logspace(1,40,5)
print(arr)
print ('%.2f'%arr[2])

arr=zeros(5);
print(arr)

arr=ones(10,int)
print(arr)

print("Operation in array using numpy")
arr=array([1,2,3])
arr=arr+10
print(arr)

ara1=array([1,2,3])
ara2=array([20,40,50])
ara3=ara1+ara2
print(ara3)

print(concatenate([ara1,ara2]))
print(sum(ara1))

print(ara1)
print(id(ara1))
print(ara2)
print( id(ara2))
print('copy start')
ara2=ara1.view()
ara3=ara2.copy()
print(id(ara2))
print(ara3)