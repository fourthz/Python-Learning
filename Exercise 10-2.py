
# Exercise 10-2

# This will read through a file of mailbox data and determine how many emails are sent each hour during the day.

# Obtain a valid file name

fname = input("Enter the file name: ")

try:
    fhand = open(fname)

except:
    print("A file named", fname, "cannot be opened.")
    quit()

# Obtain a dictionary of hours and frequency of emails per hour

email_hour = dict()

for line in fhand:

    line_list = line.split()
    
    if line_list == [] :
        continue

    elif line_list[0] == 'From' :
        email_time = line_list[5]
        time_list = email_time.split(sep = ':')
        email_hour[time_list[0]] = email_hour.get(time_list[0], 0) + 1

# Sort the dictionary by key using a list of tuples

hour_list = list()

for key, val in list(email_hour.items()) :
    hour_list.append((key, val))

hour_list.sort()

for key, val in hour_list :
    print(key, val)
