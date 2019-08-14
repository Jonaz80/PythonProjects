#count occurances of character in string
import pprint
message = input('ENter the string message you want to assess:  ')
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] +1

pprint.pprint(count)
