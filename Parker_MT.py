depth = int(input('Which number would you like to see the multiplication table for? '))
low = int(input('What is the lowest number for the table? '))
high = int(input('What is the highest number for the table? '))

for x in range(low,high):
    total = depth * x
    print(depth, '*', x, '=', total)
    x += 1
