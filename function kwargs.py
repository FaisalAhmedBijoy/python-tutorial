# # .......keyworld variable length argument -> kwargs

def student(name,**data):
    print(name)
    print(data)

    for i,j in data.items():
        print('Key : ->',i,' Value: ',j)


student('Faisal',age=28,Varsity='KUET',id=1607048)