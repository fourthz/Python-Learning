
# This is a function to calculate pay.

def computepay(hours, rate) :
    
    overtime_hours = hours - 40
    
    if overtime_hours > 0 :
        pay = 40 * rate
        pay = pay + (overtime_hours * rate * 1.5)

    else :
        pay = hours * rate

    return pay

# This is the main body of the code.
# I have included code to protect against stupid users.

my_hours = input("Enter Hours: ")
my_rate = input("Enter Rate: ")

try :
    my_hours = float(my_hours)
    my_rate = float(my_rate)
    
    print("Pay: ", computepay(my_hours, my_rate))

except :
    print("You need to enter numbers for both hours and rate.")
    