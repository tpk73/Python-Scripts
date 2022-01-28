speed = int(input('What is the speed of the vehicle in mph? '))
hour = int(input('How many hours has it traveled? '))
print('Hour    Distance Traveled')
print('-------------------------')

distance = 0

if hour != 1 :
    for x in range(1,hour) :
        distance += speed
        print(x,'     ',distance)
