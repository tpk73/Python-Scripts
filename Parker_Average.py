print('This program calculates an average grade.')
grade1 = int(input('Grade 1: '))
grade2 = int(input('Grade 2: '))
grade3 = int(input('Grade 3: '))
print('')
print('Grades to average:')
print(grade1,grade2,grade3)
print('Result:')
result = ( ( ( grade1 + grade2 ) + grade3 ))
average = ( result / 3 )
print(format(average,'.1f'))

