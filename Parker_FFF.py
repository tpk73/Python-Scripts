def main ():

    try:
        print('This program prints the contents of files listed in a file.')
        search = input('Enter the file: ')
        file_o = open(search,'r')
        content = []
        for line in file_o :
            content.append(line.rstrip())
        
        if len(content) == 0 :
            print('No files found.')
        elif len(content) ==1 :
            print(len(content), 'file found:')
        else:
            print(len(content), 'files found:')

        if len(content) > 0 :

            for element in content :
                print('\t' + element)
                file_o.close()
                
        for info in content :
            try :
                infile2 = open(info, 'r')
                print('\n''Contents of', info + ':')
                print()
                cont2 = infile2.read()
                print(cont2)
                print()
                print('------------------------------')
                infile2.close
            except :
                print('\n' + info, 'does not exist or is an invalid file.')
                print('\n''------------------------------')
                

    except IOError:
        print('No files found.')

main ()
