def main ():
    
    #counters
    upper = 0
    lower = 0
    digit = 0
    space = 0
    
    print('This program analyzes text. Enter text or enter "quit" to quit.')
    
    text = input('Please enter some text: ')
    inp = []
    
    while text != 'quit':
        for x in text:
            if x.isupper():
                upper += 1
            if x.islower():
                lower += 1
            if x.isdigit():
                digit += 1
            if x.isspace():
                space += 1
                
        text = input('Please enter some text: ')


    print('There are', upper , 'uppercase letters in this text.')
    print('There are', lower, 'lowercase letters in this text.')
    print('There are', digit, 'digits in this text.')
    print('There are', space, 'whitespace characters in this text.')

main ()
