
# This will total, count, and find the minimum and maximum of numbers entered by the user.

count = 0
total = 0

while True :
    
    user_entry = input("Enter a number: ")

    if user_entry == "done" :
        break

    try :
        num_entry = float(user_entry)

    except :
        print("Invalid input. Try again.")
        continue

    total = total + num_entry
    count = count + 1

    if count == 1 :
        min_num = num_entry
        max_num = num_entry
    elif num_entry < min_num :
        min_num = num_entry
    elif num_entry > max_num :
        max_num = num_entry

if count == 0 :
    print("No numbers were entered.")
else :
    print("Total: ", total, "   Count: ", count, "   Minimum: ", min_num, "   Maximum: ", max_num)
