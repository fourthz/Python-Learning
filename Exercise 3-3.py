# Exercise 3-3

score = input("Enter score: ")

try:

    score = float(score)

    if score > 1.0 :
        print("The score must be between 0.0 and 1.0")
    elif score >= 0.9 :
        print("Grade: A")
    elif score >= 0.8 :
        print("Grade: B")
    elif score >= 0.7 :
        print("Grade: C")
    elif score >= 0.6 :
        print("Grade: D")
    elif score >= 0.0 :
        print("Grade: F")
    else :
        print("The score must be between 0.0 and 1.0")

except:

    print("You must enter a numeric value between 0.0 and 1.0")

