def main():

    #setup
    FList = []
    MList = []
    Llist = []

    #prompt // get data
    print("enter quitJ")

    firstN = input('')

    while firstN != 'quit':
        FList.append(firstN)
        firstN = input('')

    #prompt // get data
    print("enter quitJ")

    midN = input('')

    while midN != 'quit':
        MList.append(midN)
        midN = input('')

    #prompt // get data
    print("enter quitJ")

    lastN = input('')

    while lastN != 'quit':
        Llist.append(lastN)
        lastN = input('')

    # Sorting
    FList.sort()
    MList.sort()
    Llist.sort()

    # Find Min of F,M,L names
    LenFList = len(FList)
    LenMList = len(MList)
    LenLlist = len(Llist)

    Min = min(LenFList,LenMList,LenLlist)

    # setup for output
    print('\n''Full Name\t\t' + 'Initials')
    print('-'*32)

    #print the list
    for x in range(Min):
        print(FList[x],MList[x],Llist[x] + '\t' + FList[x][0].upper()+MList[x][0].upper()+Llist[x][0].upper())

    #Overflow
    overFirst = LenFList - Min
    overMid = LenMList - Min
    overLast = LenLlist - Min

    #print overflow
    if overFirst > 0:
        print('\n''Leftover F Names')
        for x in range(overFirst):
            print(FList[Min::][x])

    if overMid > 0:
        print('\n''Leftover M Names')
        for x in range(overMid):
            print(MList[Min::][x])

    if overLast > 0:
        print('\n''Leftover L Names')
        for x in range(overLast):
            print(Llist[Min::][x])
    
    

    
main()
