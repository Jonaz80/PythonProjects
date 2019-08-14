the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# loop through list
for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type {fruit}")

# loop through lists of different types
for i in change:
    print(f"I got {i}")

#Build a list
elements = []

# use range fucntion to build the lists
# for i in range (999,990,-2):
#     print(f"adding {i} to the list")
#     elements.append(i)
#     print(f"\tThere are {len(elements)} elements in the list")
elements = list(range(1,6,2))

# now print them too
for n in elements:
    print(f"The element is: {n}")
