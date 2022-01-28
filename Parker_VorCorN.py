print('This program determines whether a character is a vowel, a consonant, or neither.')
print()
let= input('Enter a character: ')
if (let=='a' or let=='e' or let=='i' or let=='o' or let=='u' ):
     print(let,'is a vowel.')
elif let=='q' or let=='w' or let=='r' or let=='t' or let=='y' or let=='p' \
      or let=='s'  or let=='d'  or let=='f'  or let=='h' or let=='j' or let=='k' \
      or let=='l' or let=='z' or let=='x' or let=='c' or let=='v' or let=='b' \
      or let=='n' or let=='m' :
    print(let,'is a consonant.')
else :
     print(let,'is neither a vowel nor a consonant.')
