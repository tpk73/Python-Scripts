check= int(input('How many checks written for the month: '))
if(check<=20 and check>0):
    fee1= (check * .10 + 10 )
    print('Number of Checks:',check)
    print('Total Fees: ',format(fee1,'.2f'),sep='$')
elif(check>20 and check <=39):
    fee2= (check * .08 + 10 )
    print('Number of Checks:',check)
    print('Total Fees: ',format(fee2,'.2f'),sep='$')
elif(check>=40 and check<=59):
    fee3= (check * .06 + 10 )
    print('Number of Checks:',check)
    print('Total Fees: ',format(fee3,'.2f'),sep='$')
elif(check>=60):
    fee4= (check * .04 + 10 )
    print('Number of Checks:',check)
    print('Total Fees: ',format(fee4,'.2f'),sep='$')
else:
    print('Please enter a positive number.')
