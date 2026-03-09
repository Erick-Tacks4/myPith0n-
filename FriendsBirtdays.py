birthdays = {'Peter': 'April 14th', 'Erick': 'April 23rd', 'Stellah': 'January 4th'}

while True:

    name = input('Enter a friends name or (blank to quit): ')

    if name == '':
        break

    if name in birthdays:
        print(birthdays[name], ' is the birthday of ', name)

    else:
        print("I don't have the birthday information of ", name)
        print('What is their birthday?')
        bday = input('>>>')

        birthdays[name] = bday

        print('Birthday database updated')