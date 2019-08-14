birthdays = {'Alice' : 'Apr 1', 'Carol' : 'Dec 12', 'Bob' : 'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] +' is the birthday of ' +name)
    else:
        print('no birth day info for ' + name +'.')
        bday = input('What is their birthday?')
        birthdays[name] = bday
        print('Birthday dictionary updated.')
              
          
