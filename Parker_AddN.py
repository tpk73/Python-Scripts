total = 0

add = int(input('How many numbers should I add? '))

for num in range(add):
    eq = float(input('Enter a number: '))
    total += eq

print('')
print('The total is', format(total,'.1f'))
