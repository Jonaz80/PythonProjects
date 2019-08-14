from sys import argv

script, filename = argv
#opens a file in default mode (read text) & assigns it to an object txt
txt = open(filename)

print(f"Here is the content of your file {filename}:")
#uses the read method on the object txt
print(txt.read())
#closes the file
txt.close()
#below line would throw .. ValueError: I/O operation on closed file.
#print(txt.read())

# note in the below it is possible to open a file again & assign to a different object.
# print("Type the file content again?")
# file_again = input("> ")
#
# txt_again = open(file_again)
# print(txt_again.read())
