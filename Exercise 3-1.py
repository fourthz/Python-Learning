# TRENT: I DID THE FOLLOWING CODE FOR EXERCISE 3-1, THEN GOT TO EXERCISE 3-2 AND SAW THAT I HAD ALREADY DONE IT!
# YOU CAN GRADE THIS AS BOTH EXERCISES.

# This will calculate pay, including overtime pay

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try :
    hours = float(hours)
    rate = float(rate)
    
    overtime_hours = hours - 40

    if overtime_hours > 0 :
        pay = 40 * rate
        pay = pay + (overtime_hours * rate * 1.5)
    else :
        pay = hours * rate

    print("Pay: ", pay)

except :
    print("You need to enter numbers for both hours and rate.")

    