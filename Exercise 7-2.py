
# Exercise 7-2

# This will read through a file and print out the average spam confidence value.

fname = input("Enter the file name: ")

try:
    fhand = open(fname)

except:
    print("A file named", fname, "cannot be opened.")
    quit()

count = 0
total = 0

for line in fhand:

    if line.startswith('X-DSPAM-Confidence:'):
        space_pos = line.find(' ')
        num = line[(space_pos + 1):]
        count = count + 1
        total = total + float(num)

print("There are", count, "X-DSPAM-Confidence lines in", fname, "with an average confidence value of", total/count)
