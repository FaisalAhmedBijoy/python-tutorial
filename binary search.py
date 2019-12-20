# ........Binary Search

def binarySearch(list,data):


        low=0
        high=list.__len__() -1

        while(low<high):
            mid = (low + high) // 2
            if list[mid]==data :
                print('Found')
                return True
            elif data>list[mid]:
                low=mid+1
            else:
                high=mid-1

        return False

list=[10,20,30,40,50,60,70]
data=int(input('Enter The serach item'))

if binarySearch(list , data ):
    print('Found  : position',list.index(data))
else:
    print('Not Found')