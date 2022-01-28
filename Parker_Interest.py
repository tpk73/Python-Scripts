total = 0

invest = int(input('Initial investment: '))

rate = float(input('Interest rate: '))
r= (rate/100)

year = int(input('Years: '))

for x in range(year):
    money = invest * r
    invest += money

print('Your account will total $', format(invest,'.2f'), ' after ', year, ' years.' ,sep=(''))
