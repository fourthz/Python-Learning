
# Exercise 9-4

# This will read through a file of mailbox data, list who the mail is from, count how many pieces of mail are from each
# person, and then provide who sent the most messages and how many.

fname = input("Enter the file name: ")

try:
    fhand = open(fname)

except:
    print("A file named", fname, "cannot be opened.")
    quit()

emails = dict()

for line in fhand:

    line_list = line.split()
    
    if line_list == [] :
        continue

    elif line_list[0] == 'From' :
        emails[line_list[1]] = emails.get(line_list[1], 0) + 1
     
big_address = None
big_num = None

for email, num_email in emails.items() :
    if big_num is None or num_email > big_num :
        big_address = email
        big_num = num_email

print("The most email came from", big_address, "who sent you", big_num, "emails.")
