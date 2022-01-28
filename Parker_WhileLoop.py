print('This program calculates the sum of all integers from 1 to the input value.')

total=0

integer= int(input('Please enter an integer: '))

counter=1

while counter <= integer :
    total = total + counter
    counter = counter + 1

print(total)
