print('This program calculates the price to enter a zoo based on age.')
age= int(input('Enter your age: '))
if(age<=2):
    print('You entered age',age)
    print('Admission is free.')
elif(age>=3 and age<=10):
    print('You entered age',age)
    print('Admission is $5.')
elif(age>=11 and age<=20):
    print('You entered age',age)
    print('Admission is $10.')
elif(age>=21 and age<=59):
    print('You entered age',age)
    print('Admission is $20.')
elif(age>=60):
    print('You entered age',age)
    print('Admission is $10.')
