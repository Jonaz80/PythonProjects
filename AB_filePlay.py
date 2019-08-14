
inFile = open('/home/pi/Projects/PythonProjects/file.txt')

for line in inFile:
    print(line.strip().split(','))

inFile.close()

baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!\n')
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable\n')
baconFile.close()

baconFile = open('bacon.txt', 'r')
content = baconFile.read()
baconFile.close()

print(content)
