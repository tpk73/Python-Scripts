def BMI_Calculate(weight, height):
    BMI = ((weight * 703) / (height ** 2))
    print('Body Mass Indicator:', format(BMI,'.2f'))

def main():
    weight = int(input('Enter the weight: '))
    height = int(input('Enter the height: '))
    BMI_Calculate(weight,height)

main()
