print('This program calculates area or volume.')
meas= input('Would you like to calculate area or volume? ')
print()
n= 3.14
#area
if meas=='area' :
    shape= input('Would you like to calculate the area of a triangle or a circle? ')
    if shape=='triangle' :
        base= int(input('Enter the base: '))
        height= int(input('Enter the height: '))
        aot= (base * height / 2 )
        print('The area is',format(aot,'.2f'))
    elif shape=='circle' :
        radius= int(input('Enter the radius: '))
        aoc= ( n * radius ** 2)
        print('The area is',format(aoc,'.2f'))
    else :
        print('Invalid input.')
#volume
if meas=='volume' :
    shape= input('Would you like to calculate the volume of a cylinder or a sphere? ')
    if shape=='cylinder' :
        height= int(input('Enter the height: '))
        radius= int(input('Enter the radius: '))
        voc= (n * (radius**2) * height)
        print('The volume is',format(voc,'.2f'))
    elif shape=='sphere' :
        radius= int(input('Enter the radius: '))
        vos= ((4/3) * n * (radius**3))
        print('The volume is',format(vos,'.2f'))
    else :
        print('Invalid input.')

else :
    print('Invalid input.')
