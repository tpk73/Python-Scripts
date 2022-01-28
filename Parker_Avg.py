def main():

    #loop_variable
    stopper = 0

    #accumulator
    
    
    print('This program averages numbers inside a given file.')
    #infile = str(input('Enter a filename: '))
    #file = open(infile, 'r')
   
    while stopper != 1 :

        infile = input('Enter a filename: ')
        total = 0.0
        counter = 0

        if infile == 'quit' :
            stopper = 1
            
        else :
            file = open(infile, 'r')

            for x in file :
                amount = float(x)
                total += amount
                counter +=1
    
            avg = total/counter
            print('The average is',format(avg,'.2f'))

    file.close()
    
main()
