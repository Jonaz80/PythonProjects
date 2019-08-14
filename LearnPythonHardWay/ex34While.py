#
numbers = []

def counter(max, ii):
    i = 0
    while i < max:
        print(f"Ar the top i is {i}")
        numbers.append(i)

        i = i + ii
        print("Numbers now ", numbers)
        print(f"At the bottom i is {i}")


x = input("Enter a number for me to count to: > ")
inc = input("Enter a number to increment by: >")
counter(int(x), int(inc))

for num in numbers:
    print(num, end = " ")
