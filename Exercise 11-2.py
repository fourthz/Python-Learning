
# Exercise 11-2

# This will read through a file of mailbox data and determine the average of the new revision values.

# Import the regex library

import re

# Obtain a valid file name

fname = input("Enter the file name: ")

try:
    fhand = open(fname)

except:
    print("A file named", fname, "cannot be opened.")
    quit()

# Obtain a list of the new revision values.

new_revisions = list()
count_rev = 0

for line in fhand:

    line = line.rstrip()
    rev_value = re.findall('^New Revision: ([0-9.]+)', line)
    
    if len(rev_value) != 1 :
        continue

    count_rev = count_rev + 1
    rev_num = float(rev_value[0])
    new_revisions.append(rev_num)
    
# Print the average of the new revision values.

print("The average of the new revision values is", int(sum(new_revisions) / count_rev))
