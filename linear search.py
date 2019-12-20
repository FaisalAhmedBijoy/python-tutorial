print('Linear Search')
ara=[10,15,14,5,6,48]
data=int(input('Enter The Searching item'))
k=0
for i in ara:
    k=k+1
    if data==i :
        print('Data Found : index :',k)
        break
else:
    print('Not Found')
 # .............Linear search assignment -> for loop and function


def search(list , data):

    for i in list:
        if i == data:
            globals()['pos']=i
            return True

    return False

list=[10,2,101,21,56,45,48]
data=int(input('Enter The serach item'))
if search(list , data):
    print('Found  : position',list.index(data))
else:
    print('Not Found')