print('This program determines the number of letters or numbers that are in their'\
      ' correct place.')

c1= input('Enter character 1: ')
c2= input('Enter character 2: ')
c3= input('Enter character 3: ')
c4= input('Enter character 4: ')
c5= input('Enter character 5: ')

counter= 0

if c1=='1' or c1=='a' :
    counter= counter +1
if c2=='2' or c2=='b' :
    counter= counter +1
if c3=='3' or c3=='c' :
    counter= counter +1
if c4=='4' or c4=='d' :
    counter= counter +1
if c5=='5' or c5=='e' :
    counter= counter +1
    print('The number of letters or numbers in their correct places is',counter)    
else :
    print('The number of letters or numbers in their correct places is',counter)
