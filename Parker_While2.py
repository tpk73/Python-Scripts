print('This program calculates the sum of all integers from the first input value to the second input value.')

total=0

userstart= int(input('Please enter an integer: '))
userstop= int(input('Please enter an integer: '))

while userstart <= userstop :
    total+= userstart
    userstart+= 1

print(total)
