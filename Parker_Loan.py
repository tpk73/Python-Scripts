print('This program determines whether you may get a loan.')
i= int(input('Please enter your income in dollars: '))
r= int(input('Please enter your credit rating: '))
coll= input('Please enter if you are using collateral (yes or no): ')
if coll=='yes' :
    print('Approved!')
elif coll=='no' and i<50000 and r<600 :
    print('We are sorry, but you are not approved.')
elif i>=50000 and r>=600 and coll=='no' :
    print('Approved!')
elif i>=50000 and r<600 and coll=='no' :
    print('We are sorry, but you are not approved.')
elif i<50000 and r >=600 and coll=='no' :
    print('We are sorry, but you are not approved.')
