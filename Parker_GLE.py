print('This program reads in two ints and determines if they are equal.')
in1= int(input('Int 1: '))
in2= int(input('Int 2: '))
if(in1==in2):
    print(in1,'is equal to',in2)
elif(in1>=in2):
    print(in1,'is greater than',in2)
else:
    print(in1,'is less than',in2)
