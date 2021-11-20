import math
def Grade_Percentage():
    percentage = input("Enter your Grade Percentage here: ")

    if percentage == "Inc.":
        print("Grade/Mark: Inc.")
        print("Incomplete")
    elif percentage == "W":
        print("Grade/Mark: W")
        print("Withdrawn")
    elif percentage == "D":
        print("Grade/Mark: D")
        print("Dropped")
    else:
        Percentage = float(percentage)

        if Percentage >= 96.6 and Percentage <= 100:
            print("Input Grade: ", round(Percentage))
            print("Grade/Mark: 1.0")
            print("Description: Excellent")
        elif Percentage >= 93.5 and Percentage <= 96.5:
            print("Input Grade: ", round(Percentage))
            print("Grade/Mark: 1.25")
            print("Description: Excellent")
        elif Percentage >= 90.6 and Percentage <= 93.4:
            print("Input Grade: ", round(Percentage))
            print("Grade/Mark: 1.5")
            print("Description: Very Good")
        elif Percentage >= 87.5 and Percentage <= 90.5:
            print("Input Grade: ", round(Percentage))
            print("Grade/Mark: 1.75")
            print("Description: Very Good")
        elif Percentage >= 84.6 and Percentage <= 87.4:
            print("Input Grade: ", round(Percentage))
            print("Grade/Mark: 2.0")
            print("Description: Good")
        elif Percentage >= 82.5 and Percentage <= 84.5:
            print("Input Grade: ", round(Percentage))
            print("Grade/Mark: 2.25")
            print("Description: Good")
        elif Percentage >= 78.6 and Percentage <= 81.4:
            print("Input Grade: ", round(Percentage))
            print("Grade/Mark: 2.5")
            print("Description: Satisfactory")
        elif Percentage >= 75.5 and Percentage <= 78.5:
            print("Input Grade: ", round(Percentage))
            print("Grade/Mark: 2.75")
            print("Description: Satisfactory")
        elif Percentage >= 74.6 and Percentage <= 75.4:
            print("Input Grade: ", round(Percentage))
            print("Grade/Mark: 3.0")
            print("Description: Passing")
        elif Percentage >= 65 and Percentage <= 74.5:
            print("Input Grade: ", round(Percentage))
            print("Grade/Mark: 5.0")
            print("Description: Failure")

Equivalent = Grade_Percentage()
