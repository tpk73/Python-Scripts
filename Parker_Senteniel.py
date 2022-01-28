print('Enter a list of numbers, using a negative number to indicate that you are done.')

total = 0
senteniel= float(input('Enter a number: '))

while senteniel >= 0 :
    total = total + senteniel
    senteniel= float(input('Enter a number: '))
    
print('')
print('The total is', total)
