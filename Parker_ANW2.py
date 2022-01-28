def main ():

    print("Please enter some sentences. Type 'quit' on a line by itself to quit.")
    loop = input('')
    total = 0
    sent = []
    

    while loop != 'quit':
        total = total + (len(loop.split()))
        sent.append(loop)
        loop = input('')

    x = len(sent)

    print('These sentences have an average of', format(total / x ,'.2f'), 'words.')
    
        
        

main ()
