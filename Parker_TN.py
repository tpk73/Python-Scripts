def main ():

    #hold data
    PN = []
    convert = ""
    temp = []
    value = ""
    partOne = []
    partTwo = []
    partThree = []
    areaCode = []
    
    # user input
    word = input('Please enter an alphabetic telephone number:')
    
    newLetter = word.upper()

    PN.append(newLetter)

    # conversion
    # ABC = 2
    # DEF = 3
    # GHI = 4
    # JKL = 5
    # MNO = 6
    # PQRS = 7
    # TUV = 8
    # WXYZ = 9
    
    if(len(word) == 12):
        
        for x in PN:
            for y in x:
                if (y == "1"):
                    value = "1"
                    temp.append(value)
                elif (y == "A" or y == "B" or y == "C" or y == "2"):
                    value = "2"
                    temp.append(value)
                elif (y == "D" or y == "E" or y == "F" or y == "3"):
                    value = "3"
                    temp.append(value)
                elif (y == "G" or y == "H" or y == "I" or y == "4"):
                    value = "4"
                    temp.append(value)
                elif (y == "J" or y == "K" or y == "L" or y == "5"):
                    value = "5"
                    temp.append(value)
                elif (y == "M" or y == "N" or y == "O" or y == "6"):
                    value = "6"
                    temp.append(value)
                elif (y == "P" or y == "Q" or y == "R" or y == "S" or y == "7"):
                    value = "7"
                    temp.append(value)
                elif (y == "T" or y == "U" or y == "V" or y == "8"):
                    value = "8"
                    temp.append(value)
                elif (y == "W" or y == "X" or y == "Y" or y == "Z" or y == "9"):
                    value = "9"
                    temp.append(value)
                elif (y == "0"):
                    value = "0"
                    temp.append(value)

        # add -
        for x in range(0,3):
            partOne.append(temp[x])

        for x in range(3,6):
            partTwo.append(temp[x])

        for x in range(6,10):
            partThree.append(temp[x])
       
        # print
        print('The converted telephone number is ', *partOne, "-", *partTwo, "-", *partThree, sep="" , end=".")

    if(len(word) == 14):
                
        for x in PN:
            for y in x:
                if (y == "1"):
                    value = "1"
                    temp.append(value)
                elif (y == "A" or y == "B" or y == "C" or y == "2"):
                    value = "2"
                    temp.append(value)
                elif (y == "D" or y == "E" or y == "F" or y == "3"):
                    value = "3"
                    temp.append(value)
                elif (y == "G" or y == "H" or y == "I" or y == "4"):
                    value = "4"
                    temp.append(value)
                elif (y == "J" or y == "K" or y == "L" or y == "5"):
                    value = "5"
                    temp.append(value)
                elif (y == "M" or y == "N" or y == "O" or y == "6"):
                    value = "6"
                    temp.append(value)
                elif (y == "P" or y == "Q" or y == "R" or y == "S" or y == "7"):
                    value = "7"
                    temp.append(value)
                elif (y == "T" or y == "U" or y == "V" or y == "8"):
                    value = "8"
                    temp.append(value)
                elif (y == "W" or y == "X" or y == "Y" or y == "Z" or y == "9"):
                    value = "9"
                    temp.append(value)
                elif (y == "0"):
                    value = "0"
                    temp.append(value)

        # add -
        for x in range(0,1):
            areaCode.append(temp[x])

        #print(*areaCode,sep="")
        
        for x in range(1,4):
            partOne.append(temp[x])

        #print(*partOne,sep="")

        for x in range(4,7):
            partTwo.append(temp[x])

        #print(*partTwo,sep="")

        for x in range(7,11):
            partThree.append(temp[x])

        #print(*partThree,sep="")
       
        # print
        print('The converted telephone number is ', *areaCode,"-", *partOne, "-", *partTwo, "-", *partThree, sep="" , end=".")
        

main()
