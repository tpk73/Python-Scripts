def main ():
    print("Please enter some sentences. Type 'quit' on a line by itself to quit.")
    total = 0
    loop = 'y'
    sent = []
    temp = []
    count = 0

    while loop != 'quit':
        
        if loop != 'quit':
            loop = input('')
            sent.append(loop)
        else:
            quit
        count += 1

            
    for i in range(0, len(sent)):

        if sent[i] == " ":
            total = total + len(temp)
        elif sent[i] == '\t':
            total = total + len(temp)
        #temp = sent[i].split(' ')
        #temp = sent[i].split('\t')
        #total =  total + len(temp)
    
    #total = total - 1
    #print(total)
    x = int(total) - 1
    #print (x)
    #print (count)
    count -= 1
    #print (count)
    avg = x / count

    

    print('These sentences have an average of', format(avg,'.2f'), 'words.')

main ()
