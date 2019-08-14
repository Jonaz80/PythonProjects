from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}...")
#in_file = open(from_file)
indata = open(from_file).read()
print("indata..",indata)

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready... hit return to continue CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, done.")

out_file.close()
#in_file.close() # not needed if the indata is read in a single line as above
