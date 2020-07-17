
# Exercise 8-5

# This will read through a file of mailbox data, list who the mail is from, and count the number of pieces of mail.

fname = input("Enter the file name: ")

try:
    fhand = open(fname)

except:
    print("A file named", fname, "cannot be opened.")
    quit()

count = 0

for line in fhand:

    line_list = line.split()
    
    if line_list == [] :
        continue

    elif line_list[0] == 'From' :
        print(line_list[1])
        count = count + 1

print('There were', count, 'lines in the', fname, 'file that had From as the first word.')
