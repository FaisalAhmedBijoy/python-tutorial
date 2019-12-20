#.......Assignment
selectedperson=[]
def human(people):
    x=0
    for i in people:
        print('check Name : ',i)
        if len(i)>5 :
            x+=1
            selectedperson.append(i)

    return  selectedperson,x


total=int(input('Enter The total people'))
people =[]
for i in range(total):
    name=input('Enter The name')
    people.append(name)

selectedperson,selectnumber=human(people)
print('Selected total people :',selectnumber)
print('Selected person : ',selectedperson)