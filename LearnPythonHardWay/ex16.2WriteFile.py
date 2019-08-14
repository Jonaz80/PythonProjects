from sys import argv

script, filename = argv
#opens a file in read mode
txt = open(filename, 'r')

print(f"Here is the content of your file {filename}:")
#uses the read method on the object txt
print(txt.read())
#closes the file
txt.close()

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening and reading the file...")
txt = open(filename, 'r')
print(txt.read())
target = open(filename, 'w')



print("Truncating the file. Goodbye!")
#target.truncate()

print("\nprinting file content")
print(txt.read())
print("\nUh oh!!\n\n")
input("proceed?> ")

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1 +'\n' + line2 + '\n' + line3 +'\n')
print("\nprinting file content after first line, no newline")


print("\nprinting all file content")
print(txt.read())

print("And finally, we close it.")
target.close()
txt.close()
