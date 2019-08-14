from sys import argv
# read sys docs, argv is the argument variable for a script's input
#The following line unpacks the command line arguemnts into variables
script, first, second, third = argv

#looks like argv is a list...
print("script name", argv[0])

#add an input line
product = input("what shall i make with these ingredients today ...? ")

print("The script is called", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
# If there is a missing variable the scipt will complain

print(f"Here is a {product} made from {first}, {second} and {third} ...")
