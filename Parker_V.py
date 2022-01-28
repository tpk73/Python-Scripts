PI = 3.14159

def sphereVolume(radius):
    area = (((4/3) * PI) * (radius ** 3))
    return (area)

def main():
    print('This program computes the volume of a sphere.')
    radius = float(input('Enter the radius: '))
    print('The volume is', format(sphereVolume(radius),'.2f'))
    
main()
