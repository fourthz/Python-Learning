
# This will total, count, and average numbers entered by the user.

count = 0
total = 0

while True :
    
    user_entry = input("Enter a number: ")

    if user_entry == "done" :
        break

    try :
        total = total + float(user_entry)

    except :
        print("Invalid input. Try again.")
        continue

    count = count + 1

if count == 0 :
    print("No numbers were entered.")
else :
    print("Total: ", total, "   Count: ", count, "   Average", total / count)
