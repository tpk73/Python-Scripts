print('This program averages numbers.')
print('')

counter = 0
d = 0
combo = 0

x = int(input('How many numbers? '))

for num in range(x):
    d = float(input('Number: '))
    counter += 1
    combo += d
    
t = (combo/counter)

print('')
print('The average is', format(t,'.1f'))
