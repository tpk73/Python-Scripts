def main () :

    print("Please enter some numbers. Type 'q' to quit.")
    
    user_list = []
    user_input = 0
    total = 0
    
    while user_input != 'q' :

        user_input = input('Enter a number: ')
        
        if user_input != 'q' :
            
            user_input = int(user_input)
            user_list.append(int(user_input))
            total = sum(user_list)
            
        else :
            quit
  
    print('The lowest number is', min(user_list))
    print('The highest number is', max(user_list))
    print('The total of the numbers is', format(total,'.0f'))
    print('The average of the numbers is', format( sum(user_list) / len(user_list),'.2f'))

main ()
