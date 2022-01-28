def main():

#File is not reading numbers and rewriting them
#Problem Start
    
    infile = open('numbers.txt', 'r')

    print('This program displays numbers read from a file.')
    
    num = infile.readline()

    while num != '' :
        new = str(num)
        print('Number:', num.rstrip('\n'))
        num = infile.readline()

#Problem end

    infile.close()

main()
