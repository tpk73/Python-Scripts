def half_plus_seven(age):
    print('Your age is', age)
    num1 = age / 2 + 7
    return (num1)

def main():
    print('Dating age calculator.')
    num1 = int(input('Enter your age: '))
    print('Minimum age is', half_plus_seven(num1))

main()
