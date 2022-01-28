def main ():
    print('This program formats tic-tac-toe boards.')
    ttt = list(input('Enter the board: '))

    for inp1 in ttt [:3]:
        print(inp1 , end = ' ')

    print('')

    for inp2 in ttt [3:6]:
        print(inp2 , end = ' ')

    print('')

    for inp3 in ttt [6:9]:
        print(inp3 , end = ' ')

    print('')
    listprinter(ttt)

def listprinter(tictactoe):
   if type(tictactoe).__name__ != 'list':
       print('You should be using a list!')
       return False
   for element in tictactoe:
       if type(element).__name__ != 'list':
           print('You should be using a list!')
           return False
       for character in element:
           print(character,end=" ")
       print()

main ()
