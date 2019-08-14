# Add number to 100
tot = 0
# print('Enter a number: ')
num = input('Enter a number: ')
try:
    num =int(float(num))
    for i in range (1, num +1):
        tot= tot + i
    print('sum of all numbers to ' + str(num) + ' = ' + str(tot))
except:
    print('you need to enter a valid number')
