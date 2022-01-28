print('This program adds together numbers.')

string = str(input('Please enter a string of numbers:'))

total = 0

for x in string:
    total += int(x)

print('The sum of these digits is ', total ,'.',sep='')

