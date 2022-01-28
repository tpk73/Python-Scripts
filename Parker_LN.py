def main ():

    #start
    infile = input('Enter a filename: ')
    print('')
    print('Contents of',infile)

    file_c = open(infile, 'r')

    file_l = file_c.readline()
    
    
    #setup
    line_count = 0

    #startloop
    #for x in file_c :
    while file_l != '' :
        line_count +=1

        print(str(line_count)+':\t'+file_l.rstrip())
        file_l = file_c.readline()

    file_c.close()

main ()
