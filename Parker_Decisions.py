print('This program adds odd numbers, and multiplies even numbers.')
print('Enter 0 or a negative number to exit.')

math=0
usernum= int(input('Enter a positive integer: '))

while usernum > 0 :
    if (usernum % 2) == 0:
        math*=usernum
    elif (usernum % 2) != 0:
            math+=usernum
    usernum= int(input('Enter a positive integer: '))

print('The final number is', math)
