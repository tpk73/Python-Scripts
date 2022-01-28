def THR(age, restRate):
    one = 220 - age
    two = one - restRate
    three = ((two * .6) + restRate)
    print('Your training heart rate is:', format(three,'.2f'))

def main():
    age = int(input('Enter your age: '))
    restRate = int(input('Enter your resting heart rate: '))
    THR(age,restRate)

main()
