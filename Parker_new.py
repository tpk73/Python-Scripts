def main ():
    age()
    rate()
    maximum = (220 - age)
    resting = (maximum - rate)
    heart = ((resting * .6) + rate)
    print('Your training heart rate is:', heart)

def age ():
    age = int(input('Enter your age: '))

def rate ():
    rate = int(input('Enter your resting heart rate: '))
    
main()
