import sys

areasAll = {
    '1.':'Rectangle',
    '2.':'Square',
    '3.':'Circle',
    '0.':'Exit'
}


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


def mainLoop():
  print('Select the area you want to calculate.')

  for i , j in areasAll.items():
      
      print(i,'',j)
      print()
      global entry
      

while True:
    print()
    print("Hi WELCOME to area calcultions. What would you like to calculate it's area today: ")

    mainLoop()

    print('___________________________________________________________________________________')
    entry = input()
    print('___________________________________________________________________________________')

    if entry == '1':
        rectangleArea()

    elif entry == '2':
        squareArea()

    elif entry == '3':
        circleArea()

    elif entry == '0':
        sys.exit()

    else:
        print('Sorry the entry ', entry , ' you entered is invalid. Please try again with a valid entry.')

        break

input('>>>')