# ....................Matrix Operation
m=matrix(ara)
print(m)

m=matrix('1 2 3 ; 4 5 6')

m1=matrix('1 2 ; 3 4 ; 5 6')
m2=matrix('7 8 ; 9 10 ; 11 12')
m3 = m1 + m2
print('Matrix 1: \n',m1)
print('Matrix 2: \n',m2)
print('Matrix Addition 3: \n', m3)

m=matrix('1 2 3 ; 4 5 6')
print(m.min())
m1=matrix('1 2 3; 3 4 6; 5 6 7')
m2=matrix('7 8 9; 9 10 11; 11 12 13')
m3 = m1 * m2
print('Matrix 1: \n',m1)
print('Matrix 2: \n',m2)
print('Matrix 3: \n', m3)

print('Array demo Module',__name__)