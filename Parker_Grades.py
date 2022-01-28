print('This program calculates a letter grade average.')
print('Enter scores, or -1 to quit.')
print('')

total=0
average=0

grade= float(input('Enter numeric score: '))

while grade!= -1:
    total+=grade
    average+=1
    print(grade)
    print(average)
    final= (total/average)
    print(final)
    grade= float(input('Enter numeric score: '))

if final >=90:
    print('Grade: A')
elif final <90 and final >=80:
    print('Grade: B')
elif final <80 and final >=70:
    print('Grade: C')
elif final <70 and final >=60:
    print('Grade: D')
else :
    print('Grade: F')



