# Even odd function
def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd


# lst=[10,20,30,40,5,6,7,8,9,7,5]
num=int(input('Enter The Total number'))
lst=[]
for i in range(num):
    x=int(input('Enter The Numbers to count'))
    lst.append(x)

even,odd=count(lst)
print('Even : ',even ,'Odd :',odd)