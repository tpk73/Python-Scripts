def main ():

    looper = 0
    
    while looper == 0 :
            
        infile = input('Enter a filename: ')

        try:

            if infile == 'quit':
                looper = 1

            else:
                file = open(infile ,'r')

                total = 0
                counter = 0

                for x in file :
                    amount = float(x)
                    total += amount
                    counter +=1

                avg = total/counter
                print('The average is', format(avg,'.2f'))

            file.close()

        except IOError:

            loop = input('Error reading from the file. Try again? (y/n): ')

            if loop == 'y':
                looper = 0
            elif loop == 'n' :
                looper = 1

        except ValueError:

            loop = input('The file does not have proper numbers. Try again? (y/n): ')

            if loop == 'y':
                looper = 0
            elif loop == 'n':
                looper = 1
        
print('This program averages numbers inside a given file.')

main ()
