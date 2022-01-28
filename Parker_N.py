def main ():

    #setup
    flist = []
    mlist = []
    llist = []

    
    #user enters in data
    print('Enter some first names. Enter "quit" to quit.')

    first = input('')

    while first != 'quit':
        flist.append(first)
        first = input('')
            

    print('Enter some middle names. Enter "quit" to quit.')

    middle = input('')

    while middle != 'quit':
        mlist.append(middle)
        middle = input('')
            

    print('Enter some last names. Enter "quit" to quit.')

    last = input('')
    
    while last != 'quit':
        llist.append(last)
        last = input('')

    flist.sort()
    mlist.sort()
    llist.sort()

    lenflist = len(flist)
    lenmlist = len(mlist)
    lenllist = len(llist)

    fn = min(lenflist,lenmlist,lenllist)

    print('\n''Full name\t\t' + 'Initials')
    print('-'*32)

    for n in range(fn):
        print(flist[n],mlist[n],llist[n] + '\t' + flist[n][0].upper() + mlist[n][0].upper() + llist[n][0].upper())


    leftflist = lenflist - fn
    leftmlist = lenmlist - fn
    leftllist = lenllist - fn

    

    if leftflist > 0 :
        print('\n''Leftover first names:')
        for n in range(leftflist):
            print(flist[fn::][n])
    if leftmlist > 0 :
        print('\n''Leftover middle names:')
        for n in range(leftmlist):
            print(mlist[fn::][n])
    if leftllist > 0:
        print('\n''Leftover last names:')
        for n in range(leftllist):
            print(llist[fn::][n])

    
main ()
