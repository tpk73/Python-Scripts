print('This program identifies the largest of three numbers.')
print()
i1= int(input('Enter integer: '))
i2= int(input('Enter integer: '))
i3= int(input('Enter integer: '))

if(i1> i2 and i1> i3):
    print('The largest number is',i1,end='.')
if(i2> i3 and i2>i1):
    print('The largest number is',i2,end='.')
if(i3> i2 and i3>i1):
    print('The largest number is',i3,end='.')
if(i1==i2 or i1==i3 or i2==i3):
    print('The largest number is',i1 or i2,end='.')
