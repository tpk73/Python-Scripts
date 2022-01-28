print('This program averages numbers.')

sent = -1
total = 0
average = 0
num= float(input('Number: '))

while num > sent :
    total = total + num
    num= float(input('Number: '))
    average+=1
    final= (total/average)

print('')
print('The average is', format(final,'.2f'))
