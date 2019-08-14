ten_things = "Apples Oranges Crows Telephone Light Sugar"

print(f"""I need a list of ten items, so far I have {ten_things}.
Let's fix that.""")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)


print("Let's do more with lists!")

print("stuff[1]: ", stuff[1])
print("stuff[-1]: ", stuff[-1])
print(".pop() ",stuff.pop())
print("' '.join(stuff)'",' '.join(stuff))
print("'\\'.join(stuff[3:5])", '\\'.join(stuff[3:5]))
print("Sort the list: ", sorted(stuff))
print(stuff)
