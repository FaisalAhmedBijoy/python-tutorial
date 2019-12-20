a=5
b=0
try:
    print('Resouce Open')
    print(a/b)
    k=int(input('Enter a number'))
    print(k)

except ZeroDivisionError as e:
    print('Division not possible : ')

except ValueError as e:
    print('Invalid input : ',e)


except Exception as e:
    print('Exception Occur',e)

finally:
    print('Resource close')