def rectangleArea():
    lenth = int(input('Enter the Length of the rectangle: '))
    width = int(input('Enter the Width of the rectangle: '))

    area = lenth * width

    print('A rectangle with lenth ', lenth , 'and width ', width, ' has an area of: ',area)


def squareArea():
    width = int(input('Enter the width of the square: '))

    area = width * width

    print('A square with a width of ', width, ' has an area of: ', area)


def circleArea():
    radius = int(input('Enter the radius of the circle: '))

    PI = 3.142

    area = PI * radius * radius

    print('A circle with the radius of ', radius, ' has an area of: ', area)


#Usea dictionary as in ussd codes
while True:
    print("Hi WELCOME to area calcultions. What would you like to calculate it's area today: ")

    response = str(input('Enter the name of the shape: '))

    if response == 'rectangle':
        rectangleArea()

    elif response == 'square':
        squareArea()

    elif response == 'circle':
        circleArea()

    else:
        print('Sorry the response ', response , ' you entered is invalid. Please try again with a valid response.')

        break

input('>>>')