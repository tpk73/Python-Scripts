def main ():
    print('Enter a paragraph. Press enter between each line.' + \
          'Type q on a line by itself to quit.')
    text = True
    inp = []
    while text != 'q':
        if text != 'q':
            text = input()
            inp.append(text)
        else:
            quit

    print('\n''The index for this paragraph is: ')
            
    
main ()
