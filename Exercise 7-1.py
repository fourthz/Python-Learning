
# Exercise 7-1

# This will read through a file and print, line-by-line, all in upper case.

fname = input("Enter the file name: ")

try:
    fhand = open(fname)

except:
    print("A file named", fname, "cannot be opened.")
    quit()

for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print(line)
